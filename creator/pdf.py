from reportlab.pdfgen import canvas

def GeneratePdf(list, name_pdf):
    try:
        pdf = canvas.Canvas(f"{name_pdf}.pdf")
        x = 720

        for nome, idade in list.items():
            x-= 20
            pdf.drawString(247, x, f"{nome} : {idade}")

        pdf.setTitle(name_pdf)
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.drawString(247, 750, "Lista de Clientes")
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(245, 724, "Nome e Idade")
        pdf.save()

        print("Criado com sucesso")
    except:
        print("Criação falhou")


lista = { "Felipe" : "24", "José" : "42", "Maria" : "22", "Eduardo" : "31"}

GeneratePdf(lista, "Bababooey")