
from pywander.text.ref_scripts.remove_enlish_line import remove_english_line

remove_english_line('main.tex', 'main_out.tex', 'main_deleted.tex')

from pywander.text.ref_scripts.remove_redundant_blank_line import remove_redundant_blank_line


remove_redundant_blank_line('main_out.tex', 'main_out2.tex')

from pywander.text.ref_scripts.remove_unwanted_parts import remove_unwanted_parts

remove_unwanted_parts('main_out2.tex', 'main_out3.tex', 'main_deleted2.tex')

from pywander.text.ref_scripts.modify_line_to_tex_chapter import modify_line_to_tex_chapter2

modify_line_to_tex_chapter2('main_out3.tex', 'main_out4.tex')