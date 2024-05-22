class Optimizer < Formula
  include Language::Python::Virtualenv

  desc "Optimiza imágenes en la carpeta actual"
  homepage "https://github.com/javimata/homebrew-optimizer"
  url "https://github.com/javimata/homebrew-optimizer/releases/download/1.0/optimize_images-1.0.tar.gz"
  sha256 "893c8a847342c9338068dca0f93f1a27e4c2449916387725798ee8b476dc09af"
  license "MIT"

  depends_on "python@3.9"

  def install
    venv = virtualenv_create(libexec, "python3")

    # Install your script into the virtualenv
    system venv.pip_install_and_link, buildpath

    # Write out a wrapper script to launch your script
    (bin/"optimizr").write <<~EOS
      #!/bin/bash
      exec "#{libexec}/bin/python3" "#{libexec}/bin/optimize_images.py" "$@"
    EOS
  end

  test do
    system "#{bin}/optimizr", "--version"
  end
end