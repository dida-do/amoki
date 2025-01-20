The file SENTINEL2_L1C_bands.yaml is used as a source of information and reference file for the different bands available in the Sentinel2_L1C data collection. To access it in python, load it as a dictionary by using:

```python 
import yaml
from amoki.config import REFERENCES_DIR

with open(REFERENCES_DIR / 'SENTINEL2_L1C_bands.yaml') as infile:
    band_info = yaml.load(infile, Loader=yaml.FullLoader)
```

The order of bands is the same as the order returned by the get_data method of the SentinelHubRequest class. 