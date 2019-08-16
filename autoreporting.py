# this script autogenerates the report

#libraries
from jinja2 import FileSystemLoader, Environment
import pandas as pd
# import seaborn as sns
# from matplotlib import pyplot as plt

#configure display settings for pandas tables (enable wide columns)
pd.set_option("display.max_colwidth",200)

#function to turn csv file into html table
def csv_to_html(file_path, nrows = -1):
    """read in a csv file and convert it to an html string
    """
    df = pd.read_csv(file_path)
    if nrows > 0:
        df = df.head(nrows)
    html_output = df.to_html(index = False)
    return html_output


#configure the Jinja and set up the template
env = Environment(
        loader=FileSystemLoader(searchpath="templates")
)

#template that we will use
base_template = env.get_template("report.html")
table_section_template = env.get_template("table_section.html")
image_section_template = env.get_template("image_section.html")



#main function
def main():
    """
    main function: renders the template and writes it to a file
    """

    #content to be published
    #content = [1,2,3,4,5]#"This is my first report"
    title = "Report with a table section"
    sections = list()


    #modify templates in main function
    sections.append(table_section_template.render(
        table_title = "First few rows of the titanic data set",
        file_name = "train.csv",
        table = csv_to_html("data_files/train.csv", nrows = 5)
    ))

    sections.append(table_section_template.render(
        table_title = "Pclass Pivot",
        file_name = "pclass_piv.csv",
        table = csv_to_html("data_files/pclass_piv.csv")
    ))

    sections.append(image_section_template.render(
        image_title = "Pclass by Gender",
        file_name = "pclass_gender_chart.jpg",
        image = "../images/pclass_gender_chart.jpg"
    ))

    #open or generate the report file and add the content
    with open("outputs/report.html", "w") as f:
        f.write(base_template.render(
            title=title,
            sections = sections
        ))

#run the script!
if __name__ == "__main__":
    main()
    print("Done.")
