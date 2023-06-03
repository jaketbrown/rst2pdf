#!/usr/bin/env python3
import io

import atheris
import sys


with atheris.instrument_imports(include=['rst2pdf']):
    from rst2pdf.createpdf import RstToPdf

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    consumed_bytes = fdp.ConsumeBytes(fdp.remaining_bytes())
    try:
        file = io.BytesIO(consumed_bytes)
        RstToPdf(stylesheets=[]).createPdf(
            text=file.read(),
            output='/dev/null',
            source_path=None,
        )
    except Exception:
        print('FAIL')
        raise
    return

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()

