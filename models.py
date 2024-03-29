from . import db

class Pemeringkatan2019(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    KodePT = db.Column(db.String(100), unique=True)
    NamaPT = db.Column(db.String(100), unique=True)
    Jenis_PT = db.Column(db.String(100), unique=True)
    Aktif = db.Column(db.String(100), unique=True)
    Jml_Mhs = db.Column(db.String(100), unique=True)
    Jml_Dosen_Tetap = db.Column(db.String(100), unique=True)
    Jml_Dosen_Tidak_Tetap = db.Column(db.String(100), unique=True)
    DosenS3 = db.Column(db.String(100), unique=True)
    Dosen_LK_GB = db.Column(db.String(100), unique=True)
    Rasio_Dosen_Mhs = db.Column(db.String(100), unique=True)
    Mhs_Asing = db.Column(db.String(100), unique=True)
    Dosen_Asing = db.Column(db.String(100), unique=True)
    AIPT = db.Column(db.String(100), unique=True)
    APS = db.Column(db.String(100), unique=True)
    E_learning = db.Column(db.String(100), unique=True)
    Kerjasama_PT = db.Column(db.String(100), unique=True)
    Ketaatan_Lap_PDDIKTI = db.Column(db.String(100), unique=True)
    Lap_Keuangan = db.Column(db.String(100), unique=True)
    Artikel_per_dosen = db.Column(db.String(100), unique=True)
    Kinerja_Penelitian = db.Column(db.String(100), unique=True)
    Kinerja_Kemahasiswaan = db.Column(db.String(100), unique=True)
    Akreditasi_Internasional = db.Column(db.String(100), unique=True)
    Kinerja_Inovasi = db.Column(db.String(100), unique=True)
    Daya_serap_Lulusan = db.Column(db.String(100), unique=True)
    Sitasi_per_dosen = db.Column(db.String(100), unique=True)
    Paten_per_dosen = db.Column(db.String(100), unique=True)
    Kinerja_Abdimas = db.Column(db.String(100), unique=True)
    Input = db.Column(db.String(100), unique=True)
    Proses = db.Column(db.String(100), unique=True)
    Output = db.Column(db.String(100), unique=True)
    Outcome = db.Column(db.String(100), unique=True)
    Skor_Total = db.Column(db.String(100), unique=True)
    Klaster = db.Column(db.String(100), unique=True)
    Peringkat = db.Column(db.String(100), unique=True)
