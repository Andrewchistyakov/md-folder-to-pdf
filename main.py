import os
import markdown
from weasyprint import HTML


def main():
    input_folder = f'{os.path.abspath(os.getcwd())}/{input('name of .md folder >>> ')}'  # folder containing .md files
    output_folder = input('name of future .pdf folder >>> ')  # where PDFs will be saved

    # create output folder
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all .md files in input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".md"):
            # read markdown file
            md_path = os.path.join(input_folder, filename)
            with open(md_path, "r", encoding="utf-8") as f:
                md_text = f.read()

            # convert .md to HTML
            html_text = markdown.markdown(md_text)

            # generate PDF
            pdf_filename = filename.replace(".md", ".pdf")
            pdf_path = os.path.join(output_folder, pdf_filename)
            HTML(string=html_text).write_pdf(pdf_path)

            print(f"Converted: {filename} → {pdf_filename}")

    print("Finished converting!")
if __name__ == "__main__":
    main()
