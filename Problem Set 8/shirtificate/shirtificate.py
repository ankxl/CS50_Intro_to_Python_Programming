from fpdf import FPDF
from fpdf.enums import Align

def get_pdf(name):
    pdf = FPDF(orientation='P',unit='mm', format='A4')
    pdf.add_page()

    pdf.set_font("helvetica", "B", 30)
    pdf.cell(text="CS50 Shirtificate",align=Align.C,w=0)
    pdf.image('shirtificate.png',x=Align.C,y=30)
    pdf.set_font("helvetica", "",14)
    # pdf.text(0,50,"ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ")
    pdf.set_text_color(r=255, g=255, b=255)
    text = name + " took CS50"
    l = len(text)
    # pdf.cell(text=text,align=Align.C,w=0)
    pdf.text(round(((64-l)/2)*210/64,0),100,text)
    pdf.output("shirtificate.pdf")


def main():

    while True:
        if name := input('Name: '):
            break
    get_pdf(name)


if __name__ == '__main__':
    main()
