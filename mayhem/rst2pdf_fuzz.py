#!/usr/bin/env python3
import atheris
import sys

with atheris.instrument_imports(include=['rst2pdf']):
    from rst2pdf.createpdf import RstToPdf
    from reportlab.lib.styles import getSampleStyleSheet


def TestOneInput(data):
    global r2p

    fdp = atheris.FuzzedDataProvider(data)

    consumed_bool = fdp.ConsumeBool()
    consumed_sep = fdp.ConsumeString(1)
    consumed_str = fdp.ConsumeString(fdp.remaining_bytes())
    styles = getSampleStyleSheet()
    try:
        if consumed_bool:
            r2p.style_language('en')
        else:
            r2p.style_language('cn')
        r2p.author_separator(consumed_sep)
        style = styles['Normal']
        r2p.PreformattedFit(consumed_str, style)
    except ValueError:
        return
    except Exception:
        raise

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    r2p = RstToPdf(stylesheets=[])
    main()

