from markdown_pdf import MarkdownPdf, Section

pdf = MarkdownPdf()
# Replace 'your_content_here' with the content of your .md file or use the add_section method
with open("/notes.md", "r", encoding="utf-8") as f:
    markdown_content = f.read()

pdf.add_section(Section(markdown_content))
pdf.save("/Users/ashraf/Math Code Academy/Eshan/notes.pdf")
