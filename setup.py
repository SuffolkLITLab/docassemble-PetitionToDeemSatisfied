import os
import sys
from setuptools import setup, find_namespace_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.PetitionToDeemSatisfied',
      version='1.4.1',
      description=('Petition to Deem Judgment Satisfied - Massachusetts Housing Court Form'),
      long_description="# docassemble.PetitionToDeemSatisfied\r\n\r\n**Version:** 1.3.2\r\n**Author:** LIT Lab  \r\n**License:** MIT\r\n\r\n## Overview\r\n\r\nThis Docassemble interview helps tenants who have already paid an eviction judgment request that the court officially mark the judgment as satisfied. Once marked satisfied, it's easier to show future landlords or credit screeners that the case was resolved.\r\n\r\n## What This Form Does\r\n\r\nThe **Petition to Deem Judgment Satisfied** is a Massachusetts Housing Court form that allows tenants to request the court mark their eviction judgment as satisfied after full payment. This is authorized under Massachusetts General Law [Chapter 239, Section 16(k)](https://malegislature.gov/Laws/GeneralLaws/PartIII/TitleIII/Chapter239/Section16).\r\n\r\n## Who Can Use This\r\n\r\nYou are in the right place if:\r\n- The case was for nonpayment of rent\r\n- A judgment entered against you\r\n- You paid the full judgment amount (including any agreed interest or costs)\r\n\r\n## What You'll Need\r\n\r\nBefore starting, gather:\r\n- Your court papers with the docket number\r\n- Proof of payment (receipt, money order stub, bank record)\r\n- The mailing or email address for the plaintiff or their attorney\r\n\r\n## How It Works\r\n\r\nThe interview guides you through:\r\n\r\n1. **Court and case information** - Court name, docket number, and parties\r\n2. **Payment information** - Date you paid the judgment\r\n3. **Your contact information** - Address, phone, and email\r\n4. **Attorney information** (optional) - If you have an attorney\r\n5. **Service information** - How you'll notify the other party (required before filing)\r\n6. **Review and sign** - Double-check your answers and sign electronically\r\n7. **Download** - Get your completed petition ready to serve and file\r\n\r\n**Time estimate:** 10-15 minutes\r\n\r\n## Installation\r\n\r\n### For Docassemble Playground\r\n\r\n1. Download the latest release zip file (`petition_to_deem_satisfied_v1.3.1.zip`)\r\n2. Upload it to your Docassemble playground\r\n3. The interview will be available immediately\r\n\r\n### For Local Development\r\n\r\n```bash\r\npip install -e .\r\n```\r\n\r\n## Dependencies\r\n\r\n- `docassemble.AssemblyLine>=3.2.0`\r\n\r\n## Features\r\n\r\n- Left navigation sidebar for easy section tracking\r\n- Bootstrap 3 panels for clear information display\r\n- Enhanced alert cards for important tips and reminders\r\n- Conditional logic for optional attorney information\r\n- Multiple service methods (mail, email, in person)\r\n- Electronic signature support\r\n- PDF generation with properly labeled form fields\r\n\r\n## Technical Details\r\n\r\n### PDF Template\r\n\r\nThe interview uses `Petition-To-Deem-Satisfied-v1.3.pdf` with 25 properly labeled form fields:\r\n- Court information (docket number, department, division)\r\n- Party information (plaintiff, defendant/petitioner)\r\n- Payment date\r\n- Petitioner contact information\r\n- Optional attorney information\r\n- Certificate of service details\r\n\r\n\r\n## Version History\r\n\r\n- **1.3.1** - Fixed undefined `service_address` variable in review screen\r\n- **1.3** - Renamed all PDF fields to semantic names, fixed typos, standardized terminology\r\n- **1.2.1** - Enhanced intro screen with Bootstrap panels and alert cards\r\n- **1.2** - Added left navigation, removed numbered steps\r\n- **1.1** - Initial release\r\n\r\n## Support\r\n\r\nFor issues or questions, contact the LIT Lab at litlab@suffolklitlab.org\r\n\r\n## License\r\n\r\nMIT License - See LICENSE file for details\r\n",
      long_description_content_type='text/markdown',
      author='LIT Lab',
      author_email='sam.darkwa@su.suffolk.edu',
      license='MIT',
      url='https://suffolklitlab.org',
      packages=find_namespace_packages(),
      install_requires=['docassemble.AssemblyLine @ git+https://github.com/SuffolkLITLab/docassemble-AssemblyLine.git@main'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/PetitionToDeemSatisfied/', package='docassemble.PetitionToDeemSatisfied'),
     )
