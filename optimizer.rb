class Optimizer < Formula
  desc "Optimiza imágenes en la carpeta actual"
  homepage "https://github.com/javimata/homebrew-optimizer"
  url "https://github.com/javimata/homebrew-optimizer/releases/download/1.0/optimize_images-1.0.tar.gz"
  sha256 "92af80e6abb3ca9f2622bf302e667d7f31275981dfcc759653c13a2d124ccb73"
  license "MIT"

  depends_on "python@3.9"
  depends_on "pillow"

  def install
    bin.install "optimize_images.py" => "optimizer"
    (bin/"optimizer").write <<~EOS
      #!/bin/bash
      exec python3 #{prefix}/optimize_images.py "$@"
    EOS
  end

  test do
    system "#{bin}/optimizer", "--version"
  end
end
