#awal = Jl. Slamet
#tujuan = Jl. Pahlawan
#jalur

peta1 =  {'Jl. Kenanga':set(['Jl. Guntur']),
         'Jl. Guntur':set(['Jl. Slamet','Jl. Kenanga']),
         'Jl. Slamet':set(['Jl. Guntur','Jl. Bromo','Jl. Merbabu','Jl. Agung']),
         'Jl. Agung':set(['Jl. Slamet','Jl. Merapi','Jl. Merbabu','Jl. Raung']),
         'Jl. Merapi':set(['Jl. Agung']),
         'Jl. Raung':set(['Jl. Agung','Jl. Andong']),
         'Jl. Andong':set(['Jl. Raung','Merbabu']),
         'Jl. Merbabu':set(['Jl. Agung','Jl. Slamet','Jl. Andong','Jl. Siliwangi']),
         'Jl. Bromo':set(['Jl. Slamet','Jl. Pahlawan','Jl. Sriwijaya']),
         'Jl. Pahlawan':set(['Jl. Bromo']),
         'Jl. Sriwijaya':set(['Jl. Siliwangi','Jl. Bromo']),
         'Jl. Siliwangi':set(['Jl. Sriwijaya','Jl. Merbabu'])}

def bfs(graf, mulai, tujuan):
    queue = [[mulai]]
    visited = set()

    while queue:     
        # masukkan antrian paling depan ke variabel jalur
        jalur = queue.pop(0)

        # simpan node yang dipilih ke variabel state, misal jalur = C,B maka simpan B ke variabel state
        state = jalur[-1]

        # cek state apakah sama dengan tujuan, jika ya maka return jalur
        if state == tujuan:
            return jalur
        # jika state tidak sama dengan tujuan, maka cek apakah state tidak ada di visited
        elif state not in visited:
            # jika state tidak ada di visited maka cek cabang
            for cabang in graf.get(state, []): #cek semua cabang dari state
                jalur_baru = list(jalur) #masukkan isi dari variabel jalur ke variabel jalur_baru
                jalur_baru.append(cabang) #update/tambah isi jalur_baru dengan cabang
                queue.append(jalur_baru) #update/tambah queue dengan jalur_baru

            # tandai state yang sudah dikunjungi sebagai visited
            visited.add(state)

        #cek isi antrian
        isi = len(queue)
        if isi == 0:
            print("Tidak ditemukan")

print(bfs(peta1,'Jl. Slamet','Jl. Pahlawan'))
