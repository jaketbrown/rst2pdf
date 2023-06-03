#!/usr/bin/env python3
import atheris
import sys

with atheris.instrument_imports(include=['rst2pdf']):
    from rst2pdf.createpdf import RstToPdf

    # tylesheets: list = [],
    # language: str = 'en_US',
    # header: Any = None,
    # footer: Any = None,
    # inlinelinks: bool = False,
    # breaklevel: int = 1,
    # font_path: list = [],
    # style_path: list = [],
    # fit_mode: str = 'shrink',
    # background_fit_mode: str = 'center',
    # sphinx: bool = False,
    # smarty: str = '0',
    # baseurl: Any = None,
    # repeat_table_rows: bool = False,
    # footnote_backlinks: bool = True,
    # inline_footnotes: bool = False,
    # real_footnotes: bool = False,
    # def_dpi: int = 300,
    # show_frame: bool = False,
    # highlightlang: str = 'python',
    # basedir: str = os.getcwd(),
    # splittables: bool = False,
    # blank_first_page: bool = False,
    # first_page_on_right: bool = False,
    # breakside: str = 'odd',
    # custom_cover: str = 'cover.tmpl',
    # floating_images: bool = False,
    # numbered_links: bool = False,
    # section_header_depth: int = 2,
    # toc_depth: int = 0,
    # raw_html: bool = False,
    # strip_elements_with_classes: list = [],
    # record_dependencies: Any = None




def TestOneInput(data):
    global r2p

    fdp = atheris.FuzzedDataProvider(data)
    #
    consumed_bool = fdp.ConsumeBool()
    try:
        # RstToPdf(stylesheets=[]).createPdf(
        #     text=consumed_bytes,
        #     output='/dev/null',
        #     source_path=None,
        # )
        r2p.floating_images = consumed_bool

    except Exception:
        raise
    return

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    r2p = RstToPdf(stylesheets=[])
    main()

