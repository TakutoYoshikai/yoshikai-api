# yoshikai-api
This is a library to fetch Takuto Yoshikai's portfolio data.

### Usage
**install**
```bash
pip3 install git+https://github.com/TakutoYoshikai/yoshikai-api.git
```

**example**
```python
from yoshikai import yoshikai
works = yoshikai.get_ja() # fetch Japanese ver.
works = yoshikai.get_en() # fetch English ver.
```

### License
MIT License

