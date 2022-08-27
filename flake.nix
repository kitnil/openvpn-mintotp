{
  description = "Python OpenVPN with mintotp";

  outputs = { self, nixpkgs, ... }:
    (let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
      inherit (pkgs) callPackage;
    in
      {
        packages.${system} = rec {
          default = openvpn-mintotp;

          mintotp =
            callPackage
              ({ python3Packages, fetchgit }: python3Packages.buildPythonPackage rec {
                pname = "mintotp";
                version = "0.3.0";
                src = fetchgit {
                  url = "https://github.com/susam/mintotp";
                  rev = "0307b92219dccca68a6ab2dd95085834c25f2ef0";
                  sha256 = "sha256-J5a1FjDsi37uBZtkx5LyWHG2klRjUtDBYyangfR4Pnc=";
                };
              })
              {};

          openvpn-mintotp =
            callPackage
              ({ python3Packages }: python3Packages.buildPythonPackage rec {
                pname = "openvpn-mintotp";
                src = ./.;
                version = "0.0.1";
                propagatedBuildInputs = [
                  python3Packages.pexpect
                  mintotp
                ];
              })
              {};
        };
      });
}
