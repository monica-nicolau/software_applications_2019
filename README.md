# software_applications_2019
Team project for the Software Applications exam (Genomics 2019)

The project hereby presented is comprised of a website which allows the visualisation of organized data regarding chromosomes and genes present on them. The construction of the project was made possible thanks to the knowledge gained during the course "Software Applications", academic year 2019/2020.

The project consists of three parts, each carrying out a different task:

- Part 1 is the glue that holds the whole program together, connecting parts 2 and 3. This allows the data to be sorted out in the former part, and to be collected by the latter and displayed, based on the input from the user interface.
- Part 2 includes all of the Object-Oriented Programming knowledge gained throughout the course. The group decided to identify each of the eight requests in the project specification sheet in a subclass of the abstract class "Objective".The method “record” is present in each subclass but carries out a different function based on the objective that needs to be implemented by that specific subclass.
- Part 3 is responsible for the presentation of the website. It is made up of the python file together with the html files, allowing for a swift and well-organized display, avoiding a mix-up. Each input received from the user interface is sent to the Part 1 to collect the requested data and showcase it. 

By entering the website, the user can choose a category of data to be visualized in one of two manners: selection from list or choice of input. The former is the one present in the homepage and allows to pick a category of data, whilst the latter can be present once a category has been chosen, to visualise a subcategory of it.

If a slightly more detailed idea of the functioning of the website is wanted, the activity diagram (shown in the "Help" page) serves perfectly. Here the control flow lines allow for a clear understanding of the connection between the various steps (namely the activities). As the user enters the website, they will be able to choose what category of the given dataset they would like to visualise, thus leading to two possible scenarios.
The result can be either the selection of a subcategory, as previously mentioned, or the direct display of the data. If the user is then interested in further data, they will be able to go back and choose another subcategory or return to the homepage to select a completely different category. If the user is in need of help, a separate section is available for them to consult and guide them through the website.

# To run the project, enter the folder labelled "project" from the command prompt and run the python file "part3.py".
