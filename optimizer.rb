class Optimiz < Formula
  desc "Optimiza imágenes en la carpeta actual"
  homepage "https://github.com/javimata/homebrew-optimizer"
  url "https://github.com/javimata/homebrew-optimizer/releases/download/1.0/optimize_images-1.0.tar.gz"
  sha256 "1ddbdbecdc808daf8a3f0723b719c9d5a3d6e9bd50c36bfaa6e8a6e31ff74679"
  license "MIT"

  depends_on "python@3.9"

  def install
    bin.install "optimize_images.py" => "optimiz"
    chmod 0755, "#{bin}/optimiz"
  end

  test do
    system "#{bin}/optimiz", "--version"
  end
end