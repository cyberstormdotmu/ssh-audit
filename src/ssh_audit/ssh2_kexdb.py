"""
   The MIT License (MIT)

   Copyright (C) 2017-2023 Joe Testa (jtesta@positronsecurity.com)
   Copyright (C) 2017 Andris Raugulis (moo@arthepsy.eu)

   Permission is hereby granted, free of charge, to any person obtaining a copy
   of this software and associated documentation files (the "Software"), to deal
   in the Software without restriction, including without limitation the rights
   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
   copies of the Software, and to permit persons to whom the Software is
   furnished to do so, subject to the following conditions:

   The above copyright notice and this permission notice shall be included in
   all copies or substantial portions of the Software.

   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
   THE SOFTWARE.
"""
# pylint: disable=unused-import
from typing import Dict, List, Set, Sequence, Tuple, Iterable  # noqa: F401
from typing import Callable, Optional, Union, Any  # noqa: F401


class SSH2_KexDB:  # pylint: disable=too-few-public-methods
    FAIL_1024BIT_MODULUS = 'using small 1024-bit modulus'
    FAIL_3DES = 'using broken & deprecated 3DES cipher'
    FAIL_BLOWFISH = 'using weak & deprecated Blowfish cipher'
    FAIL_CAST = 'using weak & deprecated CAST cipher'
    FAIL_NSA_BACKDOORED_CURVE = 'using elliptic curves that are suspected as being backdoored by the U.S. National Security Agency'
    FAIL_DES = 'using broken DES cipher'
    FAIL_IDEA = 'using deprecated IDEA cipher'
    FAIL_LOGJAM_ATTACK = 'vulnerable to the Logjam attack: https://en.wikipedia.org/wiki/Logjam_(computer_security)'
    FAIL_MD5 = 'using broken MD5 hash algorithm'
    FAIL_PLAINTEXT = 'no encryption/integrity'
    FAIL_RC4 = 'using broken RC4 cipher'
    FAIL_RIJNDAEL = 'using deprecated & non-standardized Rijndael cipher'
    FAIL_RIPEMD = 'using deprecated RIPEMD hash algorithm'
    FAIL_SEED = 'using deprecated SEED cipher'
    FAIL_SERPENT = 'using deprecated Serpent cipher'
    FAIL_SHA1 = 'using broken SHA-1 hash algorithm'
    FAIL_SMALL_ECC_MODULUS = 'using small ECC modulus'
    FAIL_UNKNOWN = 'using unknown algorithm'
    FAIL_UNPROVEN = 'using unproven algorithm'
    FAIL_UNTRUSTED = 'using untrusted algorithm developed in secret by a government entity'

    WARN_2048BIT_MODULUS = '2048-bit modulus only provides 112-bits of symmetric strength'
    WARN_BLOCK_SIZE = 'using small 64-bit block size'
    WARN_CIPHER_MODE = 'using weak cipher mode'
    WARN_ENCRYPT_AND_MAC = 'using encrypt-and-MAC mode'
    WARN_EXPERIMENTAL = 'using experimental algorithm'
    WARN_RNDSIG_KEY = 'using weak random number generator could reveal the key'
    WARN_TAG_SIZE = 'using small 64-bit tag size'
    WARN_TAG_SIZE_96 = 'using small 96-bit tag size'

    INFO_DEFAULT_OPENSSH_CIPHER = 'default cipher since OpenSSH 6.9'
    INFO_DEFAULT_OPENSSH_KEX = 'default key exchange since OpenSSH 6.4'
    INFO_DEPRECATED_IN_OPENSSH88 = 'deprecated in OpenSSH 8.8: https://www.openssh.com/txt/release-8.8'
    INFO_DISABLED_IN_DBEAR67 = 'disabled in Dropbear SSH 2015.67'
    INFO_DISABLED_IN_OPENSSH70 = 'disabled in OpenSSH 7.0: https://www.openssh.com/txt/release-7.0'
    INFO_NEVER_IMPLEMENTED_IN_OPENSSH = 'despite the @openssh.com tag, this was never implemented in OpenSSH'
    INFO_REMOVED_IN_OPENSSH61 = 'removed since OpenSSH 6.1, removed from specification'
    INFO_REMOVED_IN_OPENSSH69 = 'removed in OpenSSH 6.9: https://www.openssh.com/txt/release-6.9'
    INFO_REMOVED_IN_OPENSSH70 = 'removed in OpenSSH 7.0: https://www.openssh.com/txt/release-7.0'
    INFO_WITHDRAWN_PQ_ALG = 'the sntrup4591761 algorithm was withdrawn, as it may not provide strong post-quantum security'


    ALGORITHMS: Dict[str, Dict[str, List[List[Optional[str]]]]] = {
        # Format: 'algorithm_name': [['version_first_appeared_in'], [reason_for_failure1, reason_for_failure2, ...], [warning1, warning2, ...], [info1, info2, ...]]
        'kex': {
            # The GSS kex algorithms get special wildcard handling, since they include variable base64 data after their standard prefixes.
            'gss-13.3.132.0.10-sha256-*': [[], [FAIL_UNKNOWN]],
            'gss-curve25519-sha256-*': [[]],
            'gss-curve448-sha512-*': [[]],
            'gss-gex-sha1-*': [[], [FAIL_SHA1]],
            'gss-gex-sha256-*': [[]],
            'gss-group1-sha1-*': [[], [FAIL_1024BIT_MODULUS, FAIL_LOGJAM_ATTACK, FAIL_SHA1]],
            'gss-group14-sha1-*': [[], [FAIL_SHA1], [WARN_2048BIT_MODULUS]],
            'gss-group14-sha256-*': [[], [], [WARN_2048BIT_MODULUS]],
            'gss-group15-sha512-*': [[]],
            'gss-group16-sha512-*': [[]],
            'gss-group17-sha512-*': [[]],
            'gss-group18-sha512-*': [[]],
            'gss-nistp256-sha256-*': [[], [FAIL_NSA_BACKDOORED_CURVE]],
            'gss-nistp384-sha256-*': [[], [FAIL_NSA_BACKDOORED_CURVE]],
            'gss-nistp521-sha512-*': [[], [FAIL_NSA_BACKDOORED_CURVE]],
            'diffie-hellman-group1-sha1': [['2.3.0,d0.28,l10.2', '6.6', '6.9'], [FAIL_1024BIT_MODULUS, FAIL_LOGJAM_ATTACK, FAIL_SHA1], [], [INFO_REMOVED_IN_OPENSSH69]],
            'diffie-hellman-group1-sha256': [[], [FAIL_1024BIT_MODULUS]],
            'diffie-hellman-group14-sha1': [['3.9,d0.53,l10.6.0'], [FAIL_SHA1], [WARN_2048BIT_MODULUS]],
            'diffie-hellman-group14-sha256': [['7.3,d2016.73'], [], [WARN_2048BIT_MODULUS]],
            'diffie-hellman-group14-sha256@ssh.com': [[], [], [WARN_2048BIT_MODULUS]],
            'diffie-hellman-group15-sha256': [[]],
            'diffie-hellman-group15-sha256@ssh.com': [[]],
            'diffie-hellman-group15-sha384@ssh.com': [[]],
            'diffie-hellman-group15-sha512': [[]],
            'diffie-hellman-group16-sha256': [[]],
            'diffie-hellman-group16-sha384@ssh.com': [[]],
            'diffie-hellman-group16-sha512': [['7.3,d2016.73']],
            'diffie-hellman-group16-sha512@ssh.com': [[]],
            'diffie-hellman-group17-sha512': [[]],
            'diffie-hellman-group18-sha512': [['7.3']],
            'diffie-hellman-group18-sha512@ssh.com': [[]],
            'diffie-hellman-group-exchange-sha1': [['2.3.0', '6.6', None], [FAIL_SHA1]],
            'diffie-hellman-group-exchange-sha256': [['4.4']],
            'diffie-hellman-group-exchange-sha256@ssh.com': [[]],
            'diffie-hellman-group-exchange-sha512@ssh.com': [[]],
            'diffie-hellman-group-exchange-sha224@ssh.com': [[]],
            'diffie-hellman-group-exchange-sha384@ssh.com': [[]],
            'diffie-hellman-group14-sha224@ssh.com': [[]],
            'diffie-hellman_group17-sha512': [[]],
            'ecmqv-sha2': [[], [FAIL_UNPROVEN]],
            'ecdh-sha2-curve25519': [[], []],
            'ecdh-sha2-nistb233': [[]],  # The NIST P-curves are suspected as being backdoored; this isn't a P-curve.
            'ecdh-sha2-nistb409': [[]],  # Not a NIST P-curve.
            'ecdh-sha2-nistk163': [[], [FAIL_SMALL_ECC_MODULUS]],    # Not a NIST P-curve.
            'ecdh-sha2-nistk233': [[]],  # Not a NIST P-curve.
            'ecdh-sha2-nistk283': [[]],  # Not a NIST P-curve.
            'ecdh-sha2-nistk409': [[]],  # Not a NIST P-curve.
            'ecdh-sha2-nistp192': [[], [FAIL_NSA_BACKDOORED_CURVE]],
            'ecdh-sha2-nistp224': [[], [FAIL_NSA_BACKDOORED_CURVE]],
            'ecdh-sha2-nistp256': [['5.7,d2013.62,l10.6.0'], [FAIL_NSA_BACKDOORED_CURVE]],
            'ecdh-sha2-nistp384': [['5.7,d2013.62'], [FAIL_NSA_BACKDOORED_CURVE]],
            'ecdh-sha2-nistp521': [['5.7,d2013.62'], [FAIL_NSA_BACKDOORED_CURVE]],
            'ecdh-sha2-nistt571': [[]],  # Not a NIST P-curve.
            'ecdh-sha2-1.3.132.0.10': [[]],  # ECDH over secp256k1 (i.e.: the Bitcoin curve)

            # Note: the base64 strings, according to draft 6 of RFC5656, is Base64(MD5(DER(OID))).  The final RFC5656 dropped the base64 strings in favor of plain OID concatenation, but apparently some SSH servers implement them anyway.  See: https://datatracker.ietf.org/doc/html/draft-green-secsh-ecc-06#section-9.2
            'ecdh-sha2-1.3.132.0.1': [[], [FAIL_SMALL_ECC_MODULUS]],  # sect163k1
            'ecdh-sha2-4MHB+NBt3AlaSRQ7MnB4cg==': [[], [FAIL_SMALL_ECC_MODULUS]],  # sect163k1
            'ecdh-sha2-1.2.840.10045.3.1.1': [[], [FAIL_SMALL_ECC_MODULUS, FAIL_NSA_BACKDOORED_CURVE]],  # NIST P-192 / secp192r1
            'ecdh-sha2-5pPrSUQtIaTjUSt5VZNBjg==': [[], [FAIL_SMALL_ECC_MODULUS, FAIL_NSA_BACKDOORED_CURVE]],  # NIST P-192 / secp192r1
            'ecdh-sha2-1.3.132.0.33': [[], [FAIL_SMALL_ECC_MODULUS, FAIL_NSA_BACKDOORED_CURVE]],  # NIST P-224 / secp224r1
            'ecdh-sha2-VqBg4QRPjxx1EXZdV0GdWQ==': [[], [FAIL_SMALL_ECC_MODULUS, FAIL_NSA_BACKDOORED_CURVE]],  # NIST P-224 / secp224r1
            'ecdh-sha2-1.3.132.0.26': [[], [FAIL_SMALL_ECC_MODULUS]],  # sect233k1
            'ecdh-sha2-zD/b3hu/71952ArpUG4OjQ==': [[], [FAIL_SMALL_ECC_MODULUS]],  # sect233k1
            'ecdh-sha2-1.3.132.0.27': [[], [FAIL_SMALL_ECC_MODULUS, FAIL_NSA_BACKDOORED_CURVE]],  # sect233r1
            'ecdh-sha2-qCbG5Cn/jjsZ7nBeR7EnOA==': [[FAIL_SMALL_ECC_MODULUS, FAIL_NSA_BACKDOORED_CURVE]],  # sect233r1
            'ecdh-sha2-1.2.840.10045.3.1.7': [[], [FAIL_NSA_BACKDOORED_CURVE]],  # NIST P-256 / secp256r1
            'ecdh-sha2-9UzNcgwTlEnSCECZa7V1mw==': [[], [FAIL_NSA_BACKDOORED_CURVE]],  # NIST P-256 / secp256r1
            'ecdh-sha2-1.3.132.0.16': [[]],  # sect283k1
            'ecdh-sha2-wiRIU8TKjMZ418sMqlqtvQ==': [[]],  # sect283k1
            'ecdh-sha2-1.3.132.0.34': [[], [FAIL_NSA_BACKDOORED_CURVE]],  # NIST P-384 / secp384r1
            'ecdh-sha2-qcFQaMAMGhTziMT0z+Tuzw==': [[], [FAIL_NSA_BACKDOORED_CURVE]],  # NIST P-384 / secp384r1
            'ecdh-sha2-1.3.132.0.36': [[]],  # sect409k1
            'ecdh-sha2-m/FtSAmrV4j/Wy6RVUaK7A==': [[]],  # sect409k1
            'ecdh-sha2-1.3.132.0.37': [[], [FAIL_NSA_BACKDOORED_CURVE]],  # sect409r1
            'ecdh-sha2-D3FefCjYoJ/kfXgAyLddYA==': [[], [FAIL_NSA_BACKDOORED_CURVE]],  # sect409r1
            'ecdh-sha2-1.3.132.0.35': [[], [FAIL_NSA_BACKDOORED_CURVE]],  # NIST P-521 / secp521r1
            'ecdh-sha2-h/SsxnLCtRBh7I9ATyeB3A==': [[], [FAIL_NSA_BACKDOORED_CURVE]],  # NIST P-521 / secp521r1
            'ecdh-sha2-1.3.132.0.38': [[]],  # sect571k1
            'ecdh-sha2-mNVwCXAoS1HGmHpLvBC94w==': [[]],  # sect571k1
            'curve25519-sha256@libssh.org': [['6.4,d2013.62,l10.6.0'], [], [], [INFO_DEFAULT_OPENSSH_KEX]],
            'curve25519-sha256': [['7.4,d2018.76'], [], [], [INFO_DEFAULT_OPENSSH_KEX]],
            'curve448-sha512': [[]],
            'kexguess2@matt.ucc.asn.au': [['d2013.57']],
            'rsa1024-sha1': [[], [FAIL_1024BIT_MODULUS, FAIL_SHA1]],
            'rsa2048-sha256': [[], [], [WARN_2048BIT_MODULUS]],
            'sntrup4591761x25519-sha512@tinyssh.org': [['8.0', '8.4'], [], [WARN_EXPERIMENTAL], [INFO_WITHDRAWN_PQ_ALG]],
            'sntrup761x25519-sha512@openssh.com': [['8.5'], [], []],
            'kexAlgoCurve25519SHA256': [[]],
            'Curve25519SHA256': [[]],
            'ext-info-c': [[]],  # Extension negotiation (RFC 8308)
            'ext-info-s': [[]],  # Extension negotiation (RFC 8308)
            'm383-sha384@libassh.org': [[], [FAIL_UNPROVEN]],
            'm511-sha512@libassh.org': [[], [FAIL_UNPROVEN]],
        },
        'key': {
            'ssh-rsa1': [[], [FAIL_SHA1]],
            'rsa-sha2-256': [['7.2']],
            'rsa-sha2-512': [['7.2']],
            'ssh-ed25519': [['6.5,l10.7.0']],
            'ssh-ed25519-cert-v01@openssh.com': [['6.5']],
            'ssh-rsa': [['2.5.0,d0.28,l10.2'], [FAIL_SHA1], [], [INFO_DEPRECATED_IN_OPENSSH88]],
            'ssh-dss': [['2.1.0,d0.28,l10.2', '6.9'], [FAIL_1024BIT_MODULUS], [WARN_RNDSIG_KEY], [INFO_DISABLED_IN_OPENSSH70]],
            'ecdsa-sha2-nistp256': [['5.7,d2013.62,l10.6.4'], [FAIL_NSA_BACKDOORED_CURVE], [WARN_RNDSIG_KEY]],
            'ecdsa-sha2-nistp384': [['5.7,d2013.62,l10.6.4'], [FAIL_NSA_BACKDOORED_CURVE], [WARN_RNDSIG_KEY]],
            'ecdsa-sha2-nistp521': [['5.7,d2013.62,l10.6.4'], [FAIL_NSA_BACKDOORED_CURVE], [WARN_RNDSIG_KEY]],
            'ecdsa-sha2-1.3.132.0.10': [[], [], [WARN_RNDSIG_KEY]],  # ECDSA over secp256k1 (i.e.: the Bitcoin curve)
            'x509v3-sign-dss': [[], [FAIL_1024BIT_MODULUS], [WARN_RNDSIG_KEY]],
            'x509v3-sign-rsa': [[], [FAIL_SHA1]],
            'x509v3-sign-rsa-sha256@ssh.com': [[]],
            'x509v3-ssh-dss': [[], [FAIL_1024BIT_MODULUS], [WARN_RNDSIG_KEY]],
            'x509v3-ssh-rsa': [[], [FAIL_SHA1], [], [INFO_DEPRECATED_IN_OPENSSH88]],
            'ssh-rsa-cert-v00@openssh.com': [['5.4', '6.9'], [FAIL_SHA1], [], [INFO_REMOVED_IN_OPENSSH70]],
            'ssh-dss-cert-v00@openssh.com': [['5.4', '6.9'], [FAIL_1024BIT_MODULUS], [WARN_RNDSIG_KEY], [INFO_DISABLED_IN_OPENSSH70]],
            'ssh-rsa-cert-v01@openssh.com': [['5.6'], [FAIL_SHA1], [], [INFO_DEPRECATED_IN_OPENSSH88]],
            'ssh-dss-cert-v01@openssh.com': [['5.6', '6.9'], [FAIL_1024BIT_MODULUS], [WARN_RNDSIG_KEY]],
            'ecdsa-sha2-nistp256-cert-v01@openssh.com': [['5.7'], [FAIL_NSA_BACKDOORED_CURVE], [WARN_RNDSIG_KEY]],
            'ecdsa-sha2-nistp384-cert-v01@openssh.com': [['5.7'], [FAIL_NSA_BACKDOORED_CURVE], [WARN_RNDSIG_KEY]],
            'ecdsa-sha2-nistp521-cert-v01@openssh.com': [['5.7'], [FAIL_NSA_BACKDOORED_CURVE], [WARN_RNDSIG_KEY]],
            'rsa-sha2-256-cert-v01@openssh.com': [['7.8']],
            'rsa-sha2-512-cert-v01@openssh.com': [['7.8']],
            'ssh-rsa-sha256@ssh.com': [[]],
            'ssh-dss-sha256@ssh.com': [[], [FAIL_1024BIT_MODULUS]],
            'sk-ecdsa-sha2-nistp256-cert-v01@openssh.com': [['8.2'], [FAIL_NSA_BACKDOORED_CURVE], [WARN_RNDSIG_KEY]],
            'sk-ecdsa-sha2-nistp256@openssh.com': [['8.2'], [FAIL_NSA_BACKDOORED_CURVE], [WARN_RNDSIG_KEY]],
            'sk-ssh-ed25519-cert-v01@openssh.com': [['8.2']],
            'sk-ssh-ed25519@openssh.com': [['8.2']],
            'ssh-gost2001': [[], [FAIL_UNTRUSTED]],
            'ssh-gost2012-256': [[], [FAIL_UNTRUSTED]],
            'ssh-gost2012-512': [[], [FAIL_UNTRUSTED]],
            'spi-sign-rsa': [[]],
            'ssh-ed448': [[]],
            'x509v3-ecdsa-sha2-nistp256': [[], [FAIL_NSA_BACKDOORED_CURVE]],
            'x509v3-ecdsa-sha2-nistp384': [[], [FAIL_NSA_BACKDOORED_CURVE]],
            'x509v3-ecdsa-sha2-nistp521': [[], [FAIL_NSA_BACKDOORED_CURVE]],
            'x509v3-rsa2048-sha256': [[]],
            'webauthn-sk-ecdsa-sha2-nistp256@openssh.com': [['8.3'], [FAIL_NSA_BACKDOORED_CURVE]],
            'ssh-xmss@openssh.com': [['7.7'], [WARN_EXPERIMENTAL]],
            'ssh-xmss-cert-v01@openssh.com': [['7.7'], [WARN_EXPERIMENTAL]],
            'dsa2048-sha224@libassh.org': [[], [FAIL_UNPROVEN], [WARN_2048BIT_MODULUS]],
            'dsa2048-sha256@libassh.org': [[], [FAIL_UNPROVEN], [WARN_2048BIT_MODULUS]],
            'dsa3072-sha256@libassh.org': [[], [FAIL_UNPROVEN]],
            'ecdsa-sha2-1.3.132.0.10-cert-v01@openssh.com': [[], [FAIL_UNKNOWN]],
            'eddsa-e382-shake256@libassh.org': [[], [FAIL_UNPROVEN]],
            'eddsa-e521-shake256@libassh.org': [[], [FAIL_UNPROVEN]],
            'null': [[], [FAIL_PLAINTEXT]],
            'pgp-sign-dss': [[], [FAIL_1024BIT_MODULUS]],
            'pgp-sign-rsa': [[], [FAIL_1024BIT_MODULUS]],
            'spki-sign-dss': [[], [FAIL_1024BIT_MODULUS]],
            'spki-sign-rsa': [[], [FAIL_1024BIT_MODULUS]],
            'ssh-dss-sha224@ssh.com': [[], [FAIL_1024BIT_MODULUS]],
            'ssh-dss-sha384@ssh.com': [[], [FAIL_1024BIT_MODULUS]],
            'ssh-dss-sha512@ssh.com': [[], [FAIL_1024BIT_MODULUS]],
            'ssh-ed448-cert-v01@openssh.com': [[], [], [], [INFO_NEVER_IMPLEMENTED_IN_OPENSSH]],
            'ssh-rsa-sha224@ssh.com': [[]],
            'ssh-rsa-sha2-256': [[]],
            'ssh-rsa-sha2-512': [[]],
            'ssh-rsa-sha384@ssh.com': [[]],
            'ssh-rsa-sha512@ssh.com': [[]],
            'x509v3-ecdsa-sha2-1.3.132.0.10': [[], [FAIL_UNKNOWN]],
            'x509v3-sign-dss-sha1': [[], [FAIL_1024BIT_MODULUS, FAIL_SHA1]],
            'x509v3-sign-dss-sha224@ssh.com': [[], [FAIL_1024BIT_MODULUS]],
            'x509v3-sign-dss-sha256@ssh.com': [[], [FAIL_1024BIT_MODULUS]],
            'x509v3-sign-dss-sha384@ssh.com': [[], [FAIL_1024BIT_MODULUS]],
            'x509v3-sign-dss-sha512@ssh.com': [[], [FAIL_1024BIT_MODULUS]],
            'x509v3-sign-rsa-sha1': [[], [FAIL_SHA1]],
            'x509v3-sign-rsa-sha224@ssh.com': [[]],
            'x509v3-sign-rsa-sha384@ssh.com': [[]],
            'x509v3-sign-rsa-sha512@ssh.com': [[]],
        },
        'enc': {
            'none': [['1.2.2,d2013.56,l10.2'], [FAIL_PLAINTEXT]],
            'des': [[], [FAIL_DES], [WARN_CIPHER_MODE, WARN_BLOCK_SIZE]],
            'des-cbc': [[], [FAIL_DES], [WARN_CIPHER_MODE, WARN_BLOCK_SIZE]],
            'des-cbc@ssh.com': [[], [FAIL_DES], [WARN_CIPHER_MODE, WARN_BLOCK_SIZE]],
            'des-cbc-ssh1': [[], [FAIL_DES], [WARN_CIPHER_MODE, WARN_BLOCK_SIZE]],
            '3des': [[], [FAIL_3DES], [WARN_CIPHER_MODE, WARN_BLOCK_SIZE]],
            '3des-cbc': [['1.2.2,d0.28,l10.2', '6.6', None], [FAIL_3DES], [WARN_CIPHER_MODE, WARN_BLOCK_SIZE]],
            '3des-ctr': [['d0.52'], [FAIL_3DES]],
            'blowfish': [[], [FAIL_BLOWFISH], [WARN_BLOCK_SIZE]],
            'blowfish-cbc': [['1.2.2,d0.28,l10.2', '6.6,d0.52', '7.1,d0.52'], [FAIL_BLOWFISH], [WARN_CIPHER_MODE, WARN_BLOCK_SIZE]],
            'blowfish-ctr': [[], [FAIL_BLOWFISH], [WARN_CIPHER_MODE, WARN_BLOCK_SIZE]],
            'twofish-cbc': [['d0.28', 'd2014.66'], [], [WARN_CIPHER_MODE], [INFO_DISABLED_IN_DBEAR67]],
            'twofish128-cbc': [['d0.47', 'd2014.66'], [], [WARN_CIPHER_MODE], [INFO_DISABLED_IN_DBEAR67]],
            'twofish192-cbc': [[], [], [WARN_CIPHER_MODE]],
            'twofish256-cbc': [['d0.47', 'd2014.66'], [], [WARN_CIPHER_MODE], [INFO_DISABLED_IN_DBEAR67]],
            'twofish-ctr': [[]],
            'twofish128-ctr': [['d2015.68']],
            'twofish192-ctr': [[]],
            'twofish256-ctr': [['d2015.68']],
            'serpent128-cbc': [[], [FAIL_SERPENT], [WARN_CIPHER_MODE]],
            'serpent192-cbc': [[], [FAIL_SERPENT], [WARN_CIPHER_MODE]],
            'serpent256-cbc': [[], [FAIL_SERPENT], [WARN_CIPHER_MODE]],
            'serpent128-ctr': [[], [FAIL_SERPENT]],
            'serpent192-ctr': [[], [FAIL_SERPENT]],
            'serpent256-ctr': [[], [FAIL_SERPENT]],
            'idea-cbc': [[], [FAIL_IDEA], [WARN_CIPHER_MODE]],
            'idea-ctr': [[], [FAIL_IDEA]],
            'cast128-ctr': [[], [FAIL_CAST]],
            'cast128-cbc': [['2.1.0', '6.6', '7.1'], [FAIL_CAST], [WARN_CIPHER_MODE, WARN_BLOCK_SIZE]],
            'arcfour': [['2.1.0', '6.6', '7.1'], [FAIL_RC4]],
            'arcfour128': [['4.2', '6.6', '7.1'], [FAIL_RC4]],
            'arcfour256': [['4.2', '6.6', '7.1'], [FAIL_RC4]],
            'aes128-cbc': [['2.3.0,d0.28,l10.2', '6.6', None], [], [WARN_CIPHER_MODE]],
            'aes192-cbc': [['2.3.0,l10.2', '6.6', None], [], [WARN_CIPHER_MODE]],
            'aes256-cbc': [['2.3.0,d0.47,l10.2', '6.6', None], [], [WARN_CIPHER_MODE]],
            'rijndael128-cbc': [['2.3.0', '7.0'], [FAIL_RIJNDAEL], [WARN_CIPHER_MODE], [INFO_DISABLED_IN_OPENSSH70]],
            'rijndael192-cbc': [['2.3.0', '7.0'], [FAIL_RIJNDAEL], [WARN_CIPHER_MODE], [INFO_DISABLED_IN_OPENSSH70]],
            'rijndael256-cbc': [['2.3.0', '7.0'], [FAIL_RIJNDAEL], [WARN_CIPHER_MODE], [INFO_DISABLED_IN_OPENSSH70]],
            'rijndael-cbc@lysator.liu.se': [['2.3.0', '6.6', '7.0'], [FAIL_RIJNDAEL], [WARN_CIPHER_MODE], [INFO_DISABLED_IN_OPENSSH70]],
            'rijndael-cbc@ssh.com': [[], [FAIL_RIJNDAEL], [WARN_CIPHER_MODE]],
            'aes128-ctr': [['3.7,d0.52,l10.4.1']],
            'aes192-ctr': [['3.7,l10.4.1']],
            'aes256-ctr': [['3.7,d0.52,l10.4.1']],
            'aes128-gcm': [[]],
            'aes256-gcm': [[]],
            'AEAD_AES_128_GCM': [[]],
            'AEAD_AES_256_GCM': [[]],
            'aes128-gcm@openssh.com': [['6.2']],
            'aes256-gcm@openssh.com': [['6.2']],
            'chacha20-poly1305': [[], [], [], [INFO_DEFAULT_OPENSSH_CIPHER]],
            'chacha20-poly1305@openssh.com': [['6.5'], [], [], [INFO_DEFAULT_OPENSSH_CIPHER]],
            'camellia128-cbc': [[], [], [WARN_CIPHER_MODE]],
            'camellia128-ctr': [[]],
            'camellia192-cbc': [[], [], [WARN_CIPHER_MODE]],
            'camellia192-ctr': [[]],
            'camellia256-cbc': [[], [], [WARN_CIPHER_MODE]],
            'camellia256-ctr': [[]],
            'crypticore128@ssh.com': [[], [FAIL_UNPROVEN]],
            'seed-cbc@ssh.com': [[], [FAIL_SEED], [WARN_CIPHER_MODE]],
            '3des-cfb': [[], [FAIL_3DES], [WARN_CIPHER_MODE]],
            '3des-ecb': [[], [FAIL_3DES], [WARN_CIPHER_MODE]],
            '3des-ofb': [[], [FAIL_3DES], [WARN_CIPHER_MODE]],
            'blowfish-cfb': [[], [FAIL_BLOWFISH], [WARN_CIPHER_MODE]],
            'blowfish-ecb': [[], [FAIL_BLOWFISH], [WARN_CIPHER_MODE]],
            'blowfish-ofb': [[], [FAIL_BLOWFISH], [WARN_CIPHER_MODE]],
            'camellia128-cbc@openssh.org': [[], [], [WARN_CIPHER_MODE]],
            'camellia128-ctr@openssh.org': [[]],
            'camellia192-cbc@openssh.org': [[], [], [WARN_CIPHER_MODE]],
            'camellia192-ctr@openssh.org': [[]],
            'camellia256-cbc@openssh.org': [[], [], [WARN_CIPHER_MODE]],
            'camellia256-ctr@openssh.org': [[]],
            'cast128-cfb': [[], [FAIL_CAST], [WARN_CIPHER_MODE]],
            'cast128-ecb': [[], [FAIL_CAST], [WARN_CIPHER_MODE]],
            'cast128-ofb': [[], [FAIL_CAST], [WARN_CIPHER_MODE]],
            'cast128-12-cbc@ssh.com': [[], [FAIL_CAST], [WARN_CIPHER_MODE]],
            'idea-cfb': [[], [FAIL_IDEA], [WARN_CIPHER_MODE]],
            'idea-ecb': [[], [FAIL_IDEA], [WARN_CIPHER_MODE]],
            'idea-ofb': [[], [FAIL_IDEA], [WARN_CIPHER_MODE]],
            'seed-ctr@ssh.com': [[], [FAIL_SEED]],
            'serpent128-gcm@libassh.org': [[], [FAIL_SERPENT]],
            'serpent256-gcm@libassh.org': [[], [FAIL_SERPENT]],
            'twofish-cfb': [[], [], [WARN_CIPHER_MODE]],
            'twofish-ecb': [[], [], [WARN_CIPHER_MODE]],
            'twofish-ofb': [[], [], [WARN_CIPHER_MODE]],
            'twofish128-gcm@libassh.org': [[]],
            'twofish256-gcm@libassh.org': [[]],
        },
        'mac': {
            'none': [['d2013.56'], [FAIL_PLAINTEXT]],
            'hmac-sha1': [['2.1.0,d0.28,l10.2'], [FAIL_SHA1], [WARN_ENCRYPT_AND_MAC]],
            'hmac-sha1-96': [['2.5.0,d0.47', '6.6', '7.1'], [FAIL_SHA1], [WARN_ENCRYPT_AND_MAC]],
            'hmac-sha1-96@openssh.com': [[], [FAIL_SHA1], [WARN_TAG_SIZE, WARN_ENCRYPT_AND_MAC], [INFO_NEVER_IMPLEMENTED_IN_OPENSSH]],
            'hmac-sha2-56': [[], [], [WARN_TAG_SIZE, WARN_ENCRYPT_AND_MAC]],
            'hmac-sha2-224': [[], [], [WARN_TAG_SIZE, WARN_ENCRYPT_AND_MAC]],
            'hmac-sha2-256': [['5.9,d2013.56,l10.7.0'], [], [WARN_ENCRYPT_AND_MAC]],
            'hmac-sha2-256-96': [['5.9', '6.0'], [], [WARN_ENCRYPT_AND_MAC], [INFO_REMOVED_IN_OPENSSH61]],
            'hmac-sha2-384': [[], [], [WARN_ENCRYPT_AND_MAC]],
            'hmac-sha2-512': [['5.9,d2013.56,l10.7.0'], [], [WARN_ENCRYPT_AND_MAC]],
            'hmac-sha2-512-96': [['5.9', '6.0'], [], [WARN_ENCRYPT_AND_MAC], [INFO_REMOVED_IN_OPENSSH61]],
            'hmac-sha3-224': [[], [], [WARN_ENCRYPT_AND_MAC]],
            'hmac-sha3-256': [[], [], [WARN_ENCRYPT_AND_MAC]],
            'hmac-sha3-384': [[], [], [WARN_ENCRYPT_AND_MAC]],
            'hmac-sha3-512': [[], [], [WARN_ENCRYPT_AND_MAC]],
            'hmac-sha256': [[], [], [WARN_ENCRYPT_AND_MAC]],
            'hmac-sha256-96@ssh.com': [[], [], [WARN_ENCRYPT_AND_MAC, WARN_TAG_SIZE]],
            'hmac-sha256@ssh.com': [[], [], [WARN_ENCRYPT_AND_MAC]],
            'hmac-sha512': [[], [], [WARN_ENCRYPT_AND_MAC]],
            'hmac-sha512@ssh.com': [[], [], [WARN_ENCRYPT_AND_MAC]],
            'hmac-md5': [['2.1.0,d0.28', '6.6', '7.1'], [FAIL_MD5], [WARN_ENCRYPT_AND_MAC]],
            'hmac-md5-96': [['2.5.0', '6.6', '7.1'], [FAIL_MD5], [WARN_ENCRYPT_AND_MAC]],
            'hmac-ripemd': [[], [FAIL_RIPEMD], [WARN_ENCRYPT_AND_MAC]],
            'hmac-ripemd160': [['2.5.0', '6.6', '7.1'], [FAIL_RIPEMD], [WARN_ENCRYPT_AND_MAC]],
            'hmac-ripemd160-96': [[], [FAIL_RIPEMD], [WARN_ENCRYPT_AND_MAC, WARN_TAG_SIZE]],
            'hmac-ripemd160@openssh.com': [['2.1.0', '6.6', '7.1'], [FAIL_RIPEMD], [WARN_ENCRYPT_AND_MAC]],
            'umac-64@openssh.com': [['4.7'], [], [WARN_ENCRYPT_AND_MAC, WARN_TAG_SIZE]],
            'umac-128@openssh.com': [['6.2'], [], [WARN_ENCRYPT_AND_MAC]],
            'hmac-sha1-etm@openssh.com': [['6.2'], [FAIL_SHA1]],
            'hmac-sha1-96-etm@openssh.com': [['6.2', '6.6', None], [FAIL_SHA1]],
            'hmac-sha2-256-96-etm@openssh.com': [[], [], [WARN_TAG_SIZE_96], [INFO_NEVER_IMPLEMENTED_IN_OPENSSH]],  # Only ever implemented in AsyncSSH (?).
            'hmac-sha2-512-96-etm@openssh.com': [[], [], [WARN_TAG_SIZE_96], [INFO_NEVER_IMPLEMENTED_IN_OPENSSH]],  # Only ever implemented in AsyncSSH (?).
            'hmac-sha2-256-etm@openssh.com': [['6.2']],
            'hmac-sha2-512-etm@openssh.com': [['6.2']],
            'hmac-md5-etm@openssh.com': [['6.2', '6.6', '7.1'], [FAIL_MD5]],
            'hmac-md5-96-etm@openssh.com': [['6.2', '6.6', '7.1'], [FAIL_MD5]],
            'hmac-ripemd160-etm@openssh.com': [['6.2', '6.6', '7.1'], [FAIL_RIPEMD]],
            'umac-32@openssh.com': [[], [], [WARN_ENCRYPT_AND_MAC, WARN_TAG_SIZE], [INFO_NEVER_IMPLEMENTED_IN_OPENSSH]],
            'umac-64-etm@openssh.com': [['6.2'], [], [WARN_TAG_SIZE]],
            'umac-96@openssh.com': [[], [], [WARN_ENCRYPT_AND_MAC], [INFO_NEVER_IMPLEMENTED_IN_OPENSSH]],
            'umac-128-etm@openssh.com': [['6.2']],
            'aes128-gcm': [[]],
            'aes256-gcm': [[]],
            'chacha20-poly1305@openssh.com': [[], [], [], [INFO_NEVER_IMPLEMENTED_IN_OPENSSH]],  # Despite the @openssh.com tag, this was never shipped as a MAC in OpenSSH (only as a cipher); it is only implemented as a MAC in Syncplify.
            'crypticore-mac@ssh.com': [[], [FAIL_UNPROVEN]],
            'AEAD_AES_128_GCM': [[]],
            'AEAD_AES_256_GCM': [[]],
            'hmac-sha224@ssh.com': [[], [], [WARN_ENCRYPT_AND_MAC]],
            'hmac-sha256-2@ssh.com': [[], [], [WARN_ENCRYPT_AND_MAC]],
            'hmac-sha384@ssh.com': [[], [], [WARN_ENCRYPT_AND_MAC]],
            'hmac-whirlpool': [[], [], [WARN_ENCRYPT_AND_MAC]],
        }
    }
