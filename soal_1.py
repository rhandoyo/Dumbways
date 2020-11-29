

def tentukan_olahraga(n):
    kalori = n
    # 1 menit itu adalah 10 kalori
    waktu_menit = int(n/10)

    if kalori > 750:
        jenis_olahraga = 'lari'
        waktu_olahraga = waktu_menit 

    elif kalori > 500:
        jenis_olahraga = 'badminton'
        waktu_olahraga = waktu_menit

    elif kalori < 500:
        jenis_olahraga = 'renang'
        waktu_olahraga = waktu_menit

    print('Jumlah kalori : ', kalori,' kalori')
    print('Jenis olahraga: ', jenis_olahraga)
    print('Waktu olahraga: ', waktu_olahraga,' Menit')

    
tentukan_olahraga(30)
