import audalign as ad
import pytest
import os

test_file = "test_audio/testers/test.mp3"
test_file2 = "test_audio/testers/pink_noise.mp3"


class TestRecognize:

    ada = ad.Audalign("test_fingerprints.json")

    @pytest.mark.smoke
    def test_recognize(self):
        assert self.ada.total_fingerprints > 0
        self.ada.set_accuracy(4)

        result = self.ada.recognize(test_file)
        assert len(result) > 1

        result2 = self.ada.recognize(test_file, filter_matches=20000)
        assert not result2

    @pytest.mark.smoke
    def test_recognize_locality(self):
        assert self.ada.total_fingerprints > 0
        self.ada.set_accuracy(4)

        result = self.ada.recognize(test_file, locality=10)
        assert len(result) > 1

    @pytest.mark.smoke
    def test_visrecognize(self):
        results = self.ada.visrecognize(
            test_file,
            test_file,
            img_width=0.5,
            volume_threshold=215,
        )
        assert results

    def test_visrecognize_options(self):
        results = self.ada.visrecognize(
            test_file,
            test_file,
            img_width=0.5,
            volume_threshold=216,
            volume_floor=100,
            vert_scaling=0.8,
            horiz_scaling=0.8,
            calc_mse=False,
        )
        assert results
        assert results["match_info"]["test.mp3"]["mse"][0] == 20000000.0

    def test_visrecognize_directory(self):
        results = self.ada.visrecognize_directory(
            test_file,
            "test_audio/testers/",
            img_width=0.5,
            volume_threshold=215,
        )
        assert results

    @pytest.mark.smoke
    def test_correcognize(self):
        results = self.ada.correcognize(
            test_file,
            test_file,
        )
        assert results

    def test_correcognize_directory(self):
        results = self.ada.correcognize_directory(
            test_file,
            "test_audio/testers/",
        )
        assert results


class TestAlign:

    ada = ad.Audalign()

    @pytest.mark.smoke
    def test_align_fingerprint(self, tmpdir):
        result = self.ada.align("test_audio/test_shifts", tmpdir)
        assert result
        result = self.ada.align(
            "test_audio/test_shifts",
            tmpdir,
            write_extension=".wav",
        )
        assert result

    def test_align_cor(self, tmpdir):
        result = self.ada.align(
            "test_audio/test_shifts", tmpdir, technique="correlation"
        )
        assert result
        result = self.ada.align(
            "test_audio/test_shifts",
            tmpdir,
            technique="correlation",
            filter_matches=0.3,  # might have to adjust this
        )
        assert result

    def test_target_align_fingerprint(self, tmpdir):
        result = self.ada.target_align(
            "test_audio/test_shifts/Eigen-song-base.mp3",
            "test_audio/test_shifts",
            destination_path=tmpdir,
        )
        assert result

    def test_target_align_vis(self, tmpdir):
        result = self.ada.target_align(
            "test_audio/test_shifts/Eigen-song-base.mp3",
            "test_audio/test_shifts",
            destination_path=tmpdir,
            technique="visual",
            img_width=0.5,
            volume_threshold=215,
        )
        assert result

    def test_target_align_cor(self, tmpdir):
        result = self.ada.target_align(
            "test_audio/test_shifts/Eigen-song-base.mp3",
            "test_audio/test_shifts",
            destination_path=tmpdir,
            technique="correlation",
        )
        assert result
