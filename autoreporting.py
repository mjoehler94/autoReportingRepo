# this script autogenerates the report

#libraries
from jinja2 import FileSystemLoader, Environment

#configure the Jinja and set up the template
env = Environment(
        loader=FileSystemLoader(searchpath="templates")
)

#template that we will use
base_template = env.get_template("report.html")
table_section_template = env.get_template("table_section.html")


#content to be published
#content = [1,2,3,4,5]#"This is my first report"
title = "Report with a table section"
sections = list()

sections.append(table_section_template.render(
    table_title = "Pclass Pivot",
    file_name = "pclasspiv.csv",
    table = "Table goes here"
))




#main function
def main():
    """
    main function: renders the template and writes it to a file
    """

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
