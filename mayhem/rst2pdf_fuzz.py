#!/usr/bin/env python3
import io

import atheris
import sys


with atheris.instrument_imports(include=['rst2pdf']):
    from rst2pdf.createpdf import RstToPdf
    from reportlab.lib.styles import getSampleStyleSheet

def TestOneInput(data):
    global r2p
    fdp = atheris.FuzzedDataProvider(data)
    ran = fdp.ConsumeIntInRange(0, 20)
    consumed_bytes = fdp.ConsumeString(fdp.ConsumeIntInRange(0, fdp.remaining_bytes()))
    try:
        if ran % 3 == 0:
            r2p.createPdf(
                text=consumed_bytes,
                output='/dev/null',
                source_path=None,
                debugLinesPdf=False
            )
        else:
            styles = getSampleStyleSheet()
            style = styles['Normal']
            r2p.PreformattedFit(consumed_bytes, style)
    except Exception:
        raise

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    r2p = RstToPdf(stylesheets=[])
    main()