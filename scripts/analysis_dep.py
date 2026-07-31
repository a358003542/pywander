"""
本脚本分析本模块包的各个子模块文件里面的其他模块依赖

"""

import os
import sys
from modulegraph.modulegraph import ModuleGraph

mg = ModuleGraph()

# 自动发现包内所有子模块
def discover_modules(pkg_dir, pkg_name):
    """返回包内所有模块的完整 dotted name"""
    modules = []
    for root, dirs, files in os.walk(pkg_dir):
        for f in files:
            if f == "__init__.py":
                # 包目录本身
                rel = os.path.relpath(root, pkg_dir)
                if rel == ".":
                    modules.append(pkg_name)
                else:
                    mod = rel.replace(os.sep, ".")
                    modules.append(f"{pkg_name}.{mod}")
            elif f.endswith(".py"):
                rel = os.path.relpath(root, pkg_dir)
                base = f[:-3]  # 去掉 .py
                if rel == ".":
                    modules.append(f"{pkg_name}.{base}")
                else:
                    mod = rel.replace(os.sep, ".")
                    modules.append(f"{pkg_name}.{mod}.{base}")
    return modules

# 发现所有子模块
all_modules = discover_modules("../pywander", "pywander")
print(f"发现 {len(all_modules)} 个子模块：")
for m in all_modules:
    print(f"  {m}")

# 逐个加入依赖图
for mod in all_modules:
    try:
        mg.import_hook(mod)
    except Exception as e:
        print(f"⚠️ 无法导入 {mod}: {e}")

# 汇总：每个子模块的第三方依赖
print("\n=== 各子模块的第三方依赖 ===")
for mod in all_modules:
    node = mg.findNode(mod)
    if node is None:
        continue
    deps = mg.getReferences(node)
    third_party = []
    for d in deps:
        ident = d.identifier
        # 过滤掉标准库和包自身
        if (not ident.startswith("pywander")) and \
           (ident not in sys.stdlib_module_names):
            third_party.append(ident)
    if third_party:
        print(f"\n📦 {mod}")
        for tp in sorted(set(third_party)):
            print(f"   → {tp}")