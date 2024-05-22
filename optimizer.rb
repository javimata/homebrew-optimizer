class Optimizer < Formula
  include Language::Python::Virtualenv

  desc "Optimiza imágenes en la carpeta actual"
  homepage "https://github.com/javimata/homebrew-optimizer"
  url "https://github.com/javimata/homebrew-optimizer/releases/download/1.0/optimize_images-1.0.tar.gz"
  sha256 "4bcb31b3ca23d6ca18db969d4c7c449634bd00ac79b7bfbdef897740e3b7d432"
  license "MIT"

  depends_on "python@3.9"
  depends_on "jpeg"
  depends_on "zlib"
  
  def install
    venv = virtualenv_create(libexec, "python3")
    venv.pip_install "pillow"
    venv.pip_install_and_link buildpath
    bin.install "optimize_images.py" => "optimizer"
    chmod 0755, "#{bin}/optimizer"
  end

  test do
    system "#{bin}/optimizer", "--version"
  end
end