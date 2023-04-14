regex_pattern = r"(?:,|\.)"	

import re
print(re.split(regex_pattern, "100,000,000.000")))
#["100", "000", "000", "000"]
