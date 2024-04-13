from bcb import sgs

# Busca a série da SELIC no SGS
selic = sgs.get({'selic':432}, start = '2010-01-01')
# Plota
if __name__ == "__main__":
    print(selic)
