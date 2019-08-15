# this script autogenerates the report

#libraries
from jinja2 import FileSystemLoader, Environment

#content to be published
content = "This is my first report"

#configure the Jinja and set up the template
env = Environment(
        loader=FileSystemLoader(searchpath="templates")
)   

template = env.get_template("report.html")



#main function
def main():
    """
    main function: renders the template and writes it to a file
    """

    #open or generate the report file and add the content
    with open("outputs/report.html", "w") as f:
        f.write(template.render(content=content))


#run the script!
if __name__ == "__main__":
    main()
    print("Done.")

