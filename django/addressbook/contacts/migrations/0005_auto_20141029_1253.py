# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20141029_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='programme',
            field=models.CharField(max_length=6, default='B4110', choices=[('', ' A4109 -Indian Institute of Technology Bhubaneswar -  Civil Engineering '), ('', ' A4111 -Indian Institute of Technology Bhubaneswar -  Electrical Engineering '), ('', ' A4125 -Indian Institute of Technology Bhubaneswar -  Mechanical Engineering '), ('', ' B4101 -Indian Institute of Technology Bombay -  Aerospace Engineering '), ('', ' B4107 -Indian Institute of Technology Bombay -  Chemical Engineering '), ('', ' B4109 -Indian Institute of Technology Bombay -  Civil Engineering '), ('', ' B4110 -Indian Institute of Technology Bombay -  Computer Science and Engineering '), ('', ' B4111 -Indian Institute of Technology Bombay -  Electrical Engineering '), ('', ' B4117 -Indian Institute of Technology Bombay -  Engineering Physics '), ('', ' B4125 -Indian Institute of Technology Bombay -  Mechanical Engineering '), ('', ' B4128 -Indian Institute of Technology Bombay -  Metallurgical Engineering and Materials Science '), ('', ' B5210 -Indian Institute of Technology Bombay -  Chemical Engineering '), ('', ' B5219 -Indian Institute of Technology Bombay -  Electrical Engineering with M.Tech. in Communications and Signal Processing'), ('', ' B5221 -Indian Institute of Technology Bombay -  Electrical Engineering with M.Tech. in Microelectronics '), ('', ' B5226 -Indian Institute of Technology Bombay -  Energy Engineering with M.Tech. in Energy Systems Engineering'), ('', ' B5229-Indian Institute of Technology Bombay -  Engineering Physics with M.Tech. in Engineering Physics with specialization in Nano Science '), ('', ' B5234 -Indian Institute of Technology Bombay -  Mechanical Engineering with M.Tech. in Computer Aided Design and Automation '), ('', ' B5235 -Indian Institute of Technology Bombay -  Mechanical Engineering with M.Tech. in Computer Integrated Manufacturing'), ('', ' B5244-Indian Institute of Technology Bombay -  Metallurgical Engineering and Materials Science with M.Tech. in Ceramics and Composites '), ('', ' B5245-Indian Institute of Technology Bombay -  Metallurgical Engineering and Materials Science with M.Tech. in Metallurgical Process Engineering '), ('', ' B5503 -Indian Institute of Technology Bombay -  Chemistry '), ('', ' D4107 -Indian Institute of Technology Delhi -  Chemical Engineering '), ('', ' D4109 -Indian Institute of Technology Delhi -  Civil Engineering '), ('', ' D4110 -Indian Institute of Technology Delhi -  Computer Science and Engineering '), ('', ' D4111 -Indian Institute of Technology Delhi -  Electrical Engineering '), ('', ' D4112 -Indian Institute of Technology Delhi -  Electrical Engineering (Power) '), ('', ' D4117 -Indian Institute of Technology Delhi -  Engineering Physics '), ('', ' D4125 -Indian Institute of Technology Delhi -  Mechanical Engineering '), ('', ' D4136 -Indian Institute of Technology Delhi -  Production and Industrial Engineering '), ('', ' D4139 -Indian Institute of Technology Delhi -  Textile Technology '), ('', ' D5205 -Indian Institute of Technology Delhi -  Biochemical Engineering and Biotechnology '), ('', ' D5210 -Indian Institute of Technology Delhi -  Chemical Engineering '), ('', ' D5216 -Indian Institute of Technology Delhi -  Computer Science and Engineering '), ('', ' D5220 -Indian Institute of Technology Delhi -  Electrical Engineering with M.Tech. in Information and Communication Technology '), ('', ' D5305 -Indian Institute of Technology Delhi -  Mathematics and Computing '), ('', ' N4107 -Indian Institute of Technology Gandhinagar -  Chemical Engineering '), ('', ' N4111 -Indian Institute of Technology Gandhinagar -  Electrical Engineering '), ('', ' N4125 -Indian Institute of Technology Gandhinagar -  Mechanical Engineering '), ('', ' W4104-Indian Institute of Technology Guwahati-  Biotechnology '), ('', ' W4107-Indian Institute of Technology Guwahati-  Chemical Engineering '), ('', ' W4108-Indian Institute of Technology Guwahati-  Chemical Science and Technology '), ('', ' W4109-Indian Institute of Technology Guwahati-  Civil Engineering '), ('', ' W4110-Indian Institute of Technology Guwahati-  Computer Science and Engineering '), ('', ' W4114-Indian Institute of Technology Guwahati-  Electronics and Communication Engineering '), ('', ' W4116-Indian Institute of Technology Guwahati-  Electronics and Electrical Engineering '), ('', ' W4117-Indian Institute of Technology Guwahati-  Engineering Physics '), ('', ' W4124-Indian Institute of Technology Guwahati-  Mathematics and Computing '), ('', ' W4125-Indian Institute of Technology Guwahati-  Mechanical Engineering '), ('', ' W4401-Indian Institute of Technology Guwahati-  Design '), ('', ' H4107-Indian Institute of Technology Hyderabad-  Chemical Engineering '), ('', ' H4109-Indian Institute of Technology Hyderabad-  Civil Engineering '), ('', ' H4110-Indian Institute of Technology Hyderabad-  Computer Science and Engineering '), ('', ' H4111-Indian Institute of Technology Hyderabad-  Electrical Engineering '), ('', ' H4118-Indian Institute of Technology Hyderabad-  Engineering Science '), ('', ' H4125-Indian Institute of Technology Hyderabad-  Mechanical Engineering '), ('', ' E4110-Indian Institute of Technology Indore-  Computer Science and Engineering '), ('', ' E4111-Indian Institute of Technology Indore-  Electrical Engineering '), ('', ' E4125-Indian Institute of Technology Indore-  Mechanical Engineering '), ('', ' K4101-Indian Institute of Technology Kanpur-  Aerospace Engineering '), ('', ' K4103-Indian Institute of Technology Kanpur-  Biological Sciences and Bioengineering '), ('', ' K4107-Indian Institute of Technology Kanpur-  Chemical Engineering '), ('', ' K4109-Indian Institute of Technology Kanpur-  Civil Engineering '), ('', ' K4110-Indian Institute of Technology Kanpur-  Computer Science and Engineering '), ('', ' K4111-Indian Institute of Technology Kanpur-  Electrical Engineering '), ('', ' K4123-Indian Institute of Technology Kanpur-  Materials Science and Engineering '), ('', ' K4125-Indian Institute of Technology Kanpur-  Mechanical Engineering '), ('', ' K4201-Indian Institute of Technology Kanpur-  Chemistry '), ('', ' K4202-Indian Institute of Technology Kanpur-  Economics '), ('', ' K4203-Indian Institute of Technology Kanpur-  Mathematics and Scientific Computing '), ('', ' K4204-Indian Institute of Technology Kanpur-  Physics '), ('', ' G4101-Indian Institute of Technology Kharagpur-  Aerospace Engineering '), ('', ' G4102-Indian Institute of Technology Kharagpur-  Agricultural and Food Engineering '), ('', ' G4105-Indian Institute of Technology Kharagpur-  Biotechnology and Biochemical Engineering '), ('', ' G4107-Indian Institute of Technology Kharagpur-  Chemical Engineering '), ('', ' G4109-Indian Institute of Technology Kharagpur-  Civil Engineering '), ('', ' G4110-Indian Institute of Technology Kharagpur-  Computer Science and Engineering '), ('', ' G4111-Indian Institute of Technology Kharagpur-  Electrical Engineering '), ('', ' G4115-Indian Institute of Technology Kharagpur-  Electronics and Electrical Communication Engineering '), ('', ' G4120-Indian Institute of Technology Kharagpur-  Industrial Engineering '), ('', ' G4121-Indian Institute of Technology Kharagpur-  Instrumentation Engineering '), ('', ' G4122-Indian Institute of Technology Kharagpur-  Manufacturing Science and Engineering '), ('', ' G4125 -Indian Institute of Technology Kharagpur-  Mechanical Engineering '), ('', ' G4127-Indian Institute of Technology Kharagpur-  Metallurgical and Materials Engineering '), ('', ' G4130-Indian Institute of Technology Kharagpur-  Mining Engineering '), ('', ' G4133-Indian Institute of Technology Kharagpur-  Ocean Engineering and Naval Architecture '), ('', ' G5101-Indian Institute of Technology Kharagpur-  Architecture '), ('', ' D5201-Indian Institute of Technology Kharagpur-  Aerospace Engineering '), ('', ' G5203-Indian Institute of Technology Kharagpur-  Agricultural and Food Engineering with M.Tech. in any of the listed specializations'), ('', ' G5208-Indian Institute of Technology Kharagpur-  Biotechnology and Biochemical Engineering '), ('', ' G5210-Indian Institute of Technology Kharagpur-  Chemical Engineering '), ('', ' G5215-Indian Institute of Technology Kharagpur-  Civil Engineering with any of the listed specialization '), ('', ' G5216-Indian Institute of Technology Kharagpur-  Computer Science and Engineering '), ('', ' G5222-Indian Institute of Technology Kharagpur-  Electrical Engineering with M.Tech. in any of the listed specializations '), ('', ' G5225 -Indian Institute of Technology Kharagpur-  Electronics and Electrical Communication Engineering with M.Tech. in any of the listed specializations'), ('', ' G5230 -Indian Institute of Technology Kharagpur-  Industrial Engineering with M.Tech. in Industrial Engineering and Management'), ('', ' G5231 -Indian Institute of Technology Kharagpur-  Manufacturing Science and Engineering with M.Tech. in Industrial Engineering and Management'), ('', ' G5239-Indian Institute of Technology Kharagpur-  Mechanical Engineering with M.Tech. in any of the listed specializations '), ('', ' G5243 -Indian Institute of Technology Kharagpur-  Metallurgical and Materials Engineering with M.Tech. in Metallurgical and Materials Engineering '), ('', ' G5247 -Indian Institute of Technology Kharagpur-  Mining Engineering '), ('', ' G5248 -Indian Institute of Technology Kharagpur-  Mining Safety Engineering '), ('', ' G5251 -Indian Institute of Technology Kharagpur-  Ocean Engineering and Naval Architecture '), ('', ' G5253 -Indian Institute of Technology Kharagpur-  Quality Engineering Design and Manufacturing '), ('', ' G5501 -Indian Institute of Technology Kharagpur-  Applied Geology '), ('', ' G5503 -Indian Institute of Technology Kharagpur-  Chemistry '), ('', ' G5504 -Indian Institute of Technology Kharagpur-  Economics '), ('', ' G5505 -Indian Institute of Technology Kharagpur-  Exploration Geophysics '), ('', ' G5506 -Indian Institute of Technology Kharagpur-  Mathematics and Computing '), ('', ' G5507 -Indian Institute of Technology Kharagpur-  Physics '), ('', ' M4101 -Indian Institute of Technology Madras -  Aerospace Engineering '), ('', ' M4107 -Indian Institute of Technology Madras -  Chemical Engineering '), ('', ' M4109 -Indian Institute of Technology Madras -  Civil Engineering '), ('', ' M4110 -Indian Institute of Technology Madras -  Computer Science and Engineering '), ('', ' M4111 -Indian Institute of Technology Madras -  Electrical Engineering '), ('', ' M4117 -Indian Institute of Technology Madras -  Engineering Physics '), ('', ' M4125 -Indian Institute of Technology Madras -  Mechanical Engineering '), ('', ' M4127 -Indian Institute of Technology Madras -  Metallurgical and Materials Engineering '), ('', ' M4132 -Indian Institute of Technology Madras -  Naval Architecture and Ocean Engineering '), ('', ' M5201 -Indian Institute of Technology Madras -  Aerospace Engineering '), ('', ' M5202 -Indian Institute of Technology Madras -  Aerospace Engineering with M.Tech. in Applied Mechanics with specialization in Biomedical Engineering '), ('', ' M5207 -Indian Institute of Technology Madras -  Biological Engineering '), ('', ' M5210 -Indian Institute of Technology Madras -  Chemical Engineering '), ('', ' M5212-Indian Institute of Technology Madras -  Civil Engineering with M.Tech. in Applied Mechanics in any of the listed specializations'), ('', ' M5213-Indian Institute of Technology Madras -  Civil Engineering (Infrastructural Civil Engineering) '), ('', ' M5215-Indian Institute of Technology Madras -  Civil Engineering with any of the listed specialization '), ('', ' M5216-Indian Institute of Technology Madras -  Computer Science and Engineering '), ('', ' M5217-Indian Institute of Technology Madras -  Electrical Engineering '), ('', ' M5218-Indian Institute of Technology Madras -  Electrical Engineering with M.Tech in Applied Mechanics with specialization in Biomedical Engineering'), ('', ' M5227-Indian Institute of Technology Madras -  Engineering Design (Automotive Engineering) '), ('', ' M5228-Indian Institute of Technology Madras -  Engineering Design (Biomedical Design) '), ('', ' M5236-Indian Institute of Technology Madras -  Mechanical Engineering (Thermal Engineering) '), ('', ' M5237-Indian Institute of Technology Madras -  Mechanical Engineering (Intelligent Manufacturing) '), ('', ' M5238-Indian Institute of Technology Madras -  Mechanical Engineering (Product design) '), ('', ' M5241-Indian Institute of Technology Madras -  Metallurgical and Materials Engineering '), ('', ' M5249-Indian Institute of Technology Madras -  Naval Architecture and Ocean Engineering '), ('', ' M5250-Indian Institute of Technology Madras -  Naval Architecture and Ocean Engineering with M.Tech in Applied Mechanics in any of the listed specializations'), ('', ' M5601-Indian Institute of Technology Madras -  Biological Sciences '), ('', ' M5602-Indian Institute of Technology Madras -  Physics '), ('', ' C4110-Indian Institute of Technology Mandi-  Computer Science and Engineering '), ('', ' C4111-Indian Institute of Technology Mandi-  Electrical Engineering '), ('', ' C4125-Indian Institute of Technology Mandi-  Mechanical Engineering '), ('', ' P4110-Indian Institute of Technology Patna-  Computer Science and Engineering '), ('', ' P4111-Indian Institute of Technology Patna-  Electrical Engineering '), ('', ' P4125-Indian Institute of Technology Patna-  Mechanical Engineering '), ('', ' J4110-Indian Institute of Technology Rajasthan-  Computer Science and Engineering '), ('', ' J4111-Indian Institute of Technology Rajasthan-  Electrical Engineering '), ('', ' J4125-Indian Institute of Technology Rajasthan-  Mechanical Engineering '), ('', ' J4138-Indian Institute of Technology Rajasthan-  Systems Science '), ('', ' R4104-Indian Institute of Technology Roorkee-  Biotechnology '), ('', ' R4107-Indian Institute of Technology Roorkee-  Chemical Engineering '), ('', ' R4109-Indian Institute of Technology Roorkee-  Civil Engineering '), ('', ' R4110-Indian Institute of Technology Roorkee-  Computer Science and Engineering '), ('', ' R4111-Indian Institute of Technology Roorkee-  Electrical Engineering '), ('', ' R4114-Indian Institute of Technology Roorkee-  Electronics and Communication Engineering '), ('', ' R4125-Indian Institute of Technology Roorkee-  Mechanical Engineering '), ('', ' R4127-Indian Institute of Technology Roorkee-  Metallurgical and Materials Engineering '), ('', ' R4135-Indian Institute of Technology Roorkee-  Polymer Science and Technology '), ('', ' R4136-Indian Institute of Technology Roorkee-  Production and Industrial Engineering '), ('', ' R4137-Indian Institute of Technology Roorkee-  Pulp and Paper Engineering '), ('', ' R5101-Indian Institute of Technology Roorkee-  Architecture '), ('', ' R5211-Indian Institute of Technology Roorkee-  Chemical Engineering with M.Tech. in Hydrocarbon Engineering'), ('', ' R5214-Indian Institute of Technology Roorkee-  Civil Engineering with M.Tech. in Structural Engineering '), ('', ' R5223-Indian Institute of Technology Roorkee-  Electrical Engineering with M.Tech. in Power Electronics '), ('', ' R5224 -Indian Institute of Technology Roorkee-  Electronics and Communication Engineering with M.Tech. in Wireless Communication'), ('', ' R5242-Indian Institute of Technology Roorkee-  Metallurgical and Materials Engineering with M.Tech. in Materials Engineering '), ('', ' R5302 -Indian Institute of Technology Roorkee-  Geological Technology '), ('', ' R5303-Indian Institute of Technology Roorkee-  Geophysical Technology '), ('', ' R5403-Indian Institute of Technology Roorkee-  Process Engineering with MBA '), ('', ' R5502-Indian Institute of Technology Roorkee-  Applied Mathematics '), ('', ' R5503-Indian Institute of Technology Roorkee-  Chemistry '), ('', ' R5507-Indian Institute of Technology Roorkee-  Physics '), ('', ' U4110-Indian Institute of Technology Ropar-  Computer Science and Engineering '), ('', ' U4111-Indian Institute of Technology Ropar-  Electrical Engineering '), ('', ' U4125-Indian Institute of Technology Ropar-  Mechanical Engineering '), ('', '  Chemical Engineering -Indian School of Mines- Dhanbad'), ('', '  Computer Science and Engineering -Indian School of Mines- Dhanbad'), ('', '  Electrical Engineering -Indian School of Mines- Dhanbad'), ('', '  Electronics and Communication Engineering -Indian School of Mines- Dhanbad'), ('', '  Environmental Engineering -Indian School of Mines- Dhanbad'), ('', '  Mechanical Engineering -Indian School of Mines- Dhanbad'), ('', '  Mineral Engineering -Indian School of Mines- Dhanbad'), ('', '  Mining Engineering -Indian School of Mines- Dhanbad'), ('', '  Mining Machinery Engineering -Indian School of Mines- Dhanbad'), ('', '  Petroleum Engineering -Indian School of Mines- Dhanbad'), ('', '  Mineral Engineering with M.Tech in Mineral Engineering -Indian School of Mines- Dhanbad'), ('', '  Mining Engineering with M.Tech. in Mining Engineering -Indian School of Mines- Dhanbad'), ('', '  Petroleum Engineering with M.Tech in Petroleum Management -Indian School of Mines- Dhanbad'), ('', '  Mathematics and Computing -Indian School of Mines- Dhanbad'), ('', '  Mineral Engineering with MBA -Indian School of Mines- Dhanbad'), ('', '  Mining Engineering with MBA -Indian School of Mines- Dhanbad'), ('', '  Applied Geology -Indian School of Mines- Dhanbad'), ('', '  Applied Geophysics -Indian School of Mines- Dhanbad'), ('', 'Varanasi-Institute of Technology- Banaras Hindu University'), ('', 'Varanasi-Institute of Technology- Banaras Hindu University'), ('', 'Varanasi-Institute of Technology- Banaras Hindu University'), ('', 'Varanasi-Institute of Technology- Banaras Hindu University'), ('', 'Varanasi-Institute of Technology- Banaras Hindu University'), ('', 'Varanasi-Institute of Technology- Banaras Hindu University'), ('', 'Varanasi-Institute of Technology- Banaras Hindu University'), ('', 'Varanasi-Institute of Technology- Banaras Hindu University'), ('', 'Varanasi-Institute of Technology- Banaras Hindu University'), ('', 'Varanasi-Institute of Technology- Banaras Hindu University'), ('', 'Varanasi-Institute of Technology- Banaras Hindu University'), ('', 'Varanasi-Institute of Technology- Banaras Hindu University'), ('', 'Varanasi-Institute of Technology- Banaras Hindu University'), ('', 'Varanasi-Institute of Technology- Banaras Hindu University'), ('', 'Varanasi-Institute of Technology- Banaras Hindu University'), ('', 'Varanasi-Institute of Technology- Banaras Hindu University'), ('', 'Varanasi-Institute of Technology- Banaras Hindu University'), ('', 'Varanasi-Institute of Technology- Banaras Hindu University'), ('', 'Varanasi-Institute of Technology- Banaras Hindu University'), ('', 'Varanasi-Institute of Technology- Banaras Hindu University'), ('', 'Varanasi-Institute of Technology- Banaras Hindu University'), ('', 'Varanasi-Institute of Technology- Banaras Hindu University'), ('', 'Varanasi-Institute of Technology- Banaras Hindu University'), ('', 'Varanasi-Institute of Technology- Banaras Hindu University')]),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='contact',
            name='gender',
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
    ]
