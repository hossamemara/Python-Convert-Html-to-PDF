# imports
import os,random,pdfkit
outputFolder=input('Please Enter The Output Folder \n')
try:
    os.remove(r'log.txt')
    print('log.txt has Removed Successfully')
except:
    print('log.txt already Removed')

with open(r'log.txt', 'a') as log:
    log.write("{}\t{}\t{}\n".format("HTML_Path","PDF_Path", 'Conversion Status'))
    log.close()
with open(r'input.txt', 'r') as input:
    for lines in input.readlines():
        print(lines.strip('\n'))
        try:
          fileName = str(random.randint(1, 1000000000))
          pdfkit.from_file(lines.strip('\n') , f"{outputFolder}\{fileName}.pdf")

          with open(r'log.txt', 'a') as log:
             log.write("{}\t{}\t{}\n".format(lines.strip('\n'),f"{outputFolder}\{fileName}.pdf",'Converted Successfully'))
             log.close()


        except Exception as exception:
            with open(r'log.txt', 'a') as log:

                log.write("{}\t{}\t{}\n".format(lines.strip('\n'), f"{outputFolder}\{fileName}.pdf", 'Conversion Failed'))
                log.close()
            print("Exception message: {}".format(exception))











