# 调用说明

```python
from Signalway import SwExcel

if __name__ == '__main__':
    excel = SwExcel()
    excel.insertRows([['Number6',2, 40, 30],['data6',3, 40, 25]])
    excel.save('test.xlsx')
```
