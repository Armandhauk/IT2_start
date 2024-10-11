import pylab as pl

# Informasjon om bevegelsen
s = 0.0  # startposisjon, m
v = 5.0  # startfart, m/s
a = 2.0  # akselerasjon, m/s^2
t = 0.0  # starttid, s

# Simuleringsteknisk
t_slutt = 3.0    # sluttid, s
dt = 0.1         # lengde på tidssteg, s
t_verdier = [t]  # liste hvor verdiene av t legges inn
s_verdier = [s]  # liste hvor verdiene av s legges inn

# Løkka regner ut ny posisjon for hvert tidssteg
while t < t_slutt:
  v = v + a*dt         # beregner ny fart
  s = s + v*dt         # beregner ny posisjon
  t = t + dt           # tiden økes med dt
  t_verdier.append(t)  # legger t inn i tidslisten
  s_verdier.append(s)  # legger s inn i posisjonslisten

# Tegning av graf
pl.plot(t_verdier, s_verdier)              # lager grafen
pl.title("Strekning som funksjon av tid")  # tittel på grafen
pl.xlabel("$t$ (s)")                       # x-akse-tittel, $ gir kursiv
pl.ylabel("$s$ (m)")                       # y-akse-tittel
pl.grid()                                  # legger til rutenett
pl.show()                                  # viser grafen