import pdfkit

#Define path to wkhtmltopdf.exe
path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

#Define url
url = 'https://www.toptal.com/nodejs/why-the-hell-would-i-use-node-js#:~:text=js%20used%20for%3F-,Node.,push%2Dbased%20architectures%20in%20mind.'

#Point pdfkit configuration to wkhtmltopdf.exe
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

#Convert Webpage to PDF
pdfkit.from_url(url, output_path='./downloads/webpage.pdf', configuration=config)