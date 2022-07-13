resume_text_having_experiences = """
Experience
Clinical Laboratory Scientist,
Children's National Medical Center, Washington, DC
(April 2000 - Present)
Performs and evaluates routine and complex laboratory procedures in
hematology, coagulation, clinical chemistry, urinalysis, and
microbiology. Reports results to physicians and nursing staff. Maintains
equipment and supplies.
Performs quality control procedures and preventive maintenance on
instruments. Monitors laboratory quality assurance programs. Participates in
proficiency testing programs. Assures compliance with hospital and laboratory
safety policies and procedures.

Research Technician,
National Institute of Health, Bethesda, MD
(July 1999 - March 2000)
Performed research on the genetic causes of obesity in mice.
Assisted in the design and execution of experiments.
Maintained a detailed database of experimental results.

Research Assistant,
National Institute of Health, Bethesda, MD
(June 1998 - June 1999)
Performed standard molecular biology techniques including DNA and RNA
extraction, PCR, and gel electrophoresis.
Cloned and sequenced DNA fragments.
Conducted literature searches and synthesized information for grant proposals.

Research Assistant,
University of Maryland, College Park, MD
(September 1994 - May 1998)
Performed standard molecular biology techniques.
Conducted baseline studies on the development of the zebrafish
embryo.
Cloned and sequenced DNA fragments.
"""


import re

def extract_dates(text):
    months_num = r'(01)|(02)|(03)|(04)|(05)|(06)|(07)|(08)|(09)|(10)|(11)|(12)'
    months_short = r'(jan)|(feb)|(mar)|(apr)|(may)|(jun)|(jul)|(aug)|(sep)|(oct)|(nov)|(dec)'
    months_long = r'(january)|(february)|(march)|(april)|(may)|(june)|(july)|(august)|(september)|(october)|(november)|(december)'
    month = r'(' + months_num + r'|' + months_short + r'|' + months_long + r')'
    regex_year = r'((20|19)(\d{2})|(\d{2}))'
    year = regex_year





    start_date = month + not_alpha_numeric + r"?" + year
    end_date = r'((' + number + r'?' + not_alpha_numeric + r"?" + month + not_alpha_numeric + r"?" + year + r')|(present|current|till date|today))'
    longer_year = r"((20|19)(\d{2}))"
    year_range = longer_year + r"(" + not_alpha_numeric + r"{1,4}|(\s*to\s*))" + r'(' + longer_year + r'|(present|current|till date|today))'

    date_range = r"(" + start_date + r"(" + not_alpha_numeric + r"{1,4}|(\s*to\s*))" + end_date + r")|(" + year_range + r")"
    regular_expression = re.compile(date_range, re.IGNORECASE)

    regex_result = re.search(regular_expression, resume_text)