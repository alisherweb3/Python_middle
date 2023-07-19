# has a question about zip massive file
[(datetime(2020, 1, 1), datetime(2020, 1, 7)), (datetime(2020, 1, 15), datetime(2020, 2, 7))]

# answer

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple

@dataclass
class Movie:
  title: str
  date: List[Tuple[datetime, datetime]]

  def schedule(self) -> Generator[datetime, None, None]:
    delta = timedelta(days=1)
    for start_date, end_date in self.dates:
      while start_date <= end_date:
        yield start_date
        start_data += delta
