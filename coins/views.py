from django.shortcuts import render


class Coin():
  def __init__(self, title, year, notes, face_value, appraised_value):
    self.title = title
    self.year = year
    self.notes = notes
    self.face_value = face_value
    self.appraised_value = appraised_value
    
  def get_appreciation_percentage(self):
    return self.appraised_value / self.face_value

coins=[
  Coin('Canadian Silver Dollar', '1956', 'Purchased 1980 for 1 dollar', 1.00, 2.10),
  Coin('American Silver Eagle', '1986', 'Purchased 1986 for 1 dollar, Uncirculated', 1.00, 45.00),
  Coin('American Wheat Penny', '1933', 'Found in old car.', .01, 3.79),
  Coin('Mercury Dime', '1943', 'Found in loose change', .10 , 2.50),
  Coin('Canadian Penny', '1981', 'Found in loose change', .01 , .01),
  Coin('American V Nickle', '1912', 'cut in half', .05 , .02),

]


def home(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def coins_index(request):
  return render(request, 'coins/index.html', {'coins': coins})
