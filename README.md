# Python-Convert-Html-to-PDF
<h1>This Tool Converts HTML Files To PDF</h1>
<h2>Conversion in 3 Steps from Webpage/HTML to PDF</h2>
<h3>Step1: Download library pdfkit</h3>
<p>Comand: $ pip install pdfkit</p>
<h3>Step1: Download library pdfkit</h3>
<p>Comand: $ pip install pdfkit</p>
<h3>Step2: Download wkhtmltopdf</h3>
<h6>For Ubuntu/Debian:</h6>
<p>sudo apt-get install wkhtmltopdf</p>
<h6>For Windows:</h6>
<p>(a)Download link: <a
    href="https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_msvc2015-win64.exe"
    target="_blank"></a></p>
<p>(b)Set: PATH variable set binary folder in Environment variables.
</p>   
<h3>Step3: Code in Python to Download:</h3>
<h4>(i) Already Saved HTML page</h4>
<pre>import pdfkit
     pdfkit.from_file('test.html', 'out.pdf')</pre>
