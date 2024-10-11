sommer_ol = [
  { "årstall": 2004, "vinnertider": { "100 m": 10.93, "200 m": 22.06, "400 m": 49.41 } },
  { "årstall": 2008, "vinnertider": { "100 m": 10.78, "200 m": 21.74, "400 m": 49.62 } },
  { "årstall": 2012, "vinnertider": { "100 m": 10.75, "200 m": 21.88, "400 m": 49.55 } },
  { "årstall": 2016, "vinnertider": { "100 m": 10.71, "200 m": 21.78, "400 m": 49.44 } },
  { "årstall": 2020, "vinnertider": { "100 m": 10.61, "200 m": 21.53, "400 m": 48.36 } }
]

for ol in sommer_ol:
  år=sommer_ol[4]["årstall"]
  vinnertider100m=sommer_ol[4]["vinnertider"]["100 m"]
  vinnertider200m=sommer_ol[4]["vinnertider"]["200 m"]
  vinnertider400m=sommer_ol[4]["vinnertider"]["400 m"]

print(f"i {år}, var vinnertiden på 100 m {vinnertider100m}s 200 m {vinnertider200m}s og 400 m {vinnertider400m}s")
