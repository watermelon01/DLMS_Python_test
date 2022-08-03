class dlmsErrors:

    forever_halt_1 = [
        # 01. AARQ: AA={16,1}, No-Ciphering,No-Auth
        "0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000",
        # 01. Get: {1,0-0:42.0.0.255,2} (LDN)
        "000100100001000dc001c1000100002a0000ff0200",
        # 02. Corrupted client/server addresses (two bits flip)
        "000100110002000dc001c100010000000200ff0200",
        # 03. RLRQ
        "00010010000100026200",
        # 04. AARQ: AA={16,1}, No-Ciphering,No-Auth
        "0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000",
        # 05. Get: {1,0-0:42.0.0.255,2} (LDN)
        "000100100001000dc001c1000100002a0000ff0200",
        # 06. Zero-length payload; corrupted client address
        "0001001200010000",
        # 07. RLRQ
        "00010010000100026200",
        # 08. None-DLMS but a valid WPDU; Corrupted client/server addresses (two bits
        # flip)
        "000100130002000a00010203040506070809",
        # 09. AARQ: AA={16,1}, No-Ciphering,No-Auth
        "0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000",
        # 10. Get: {1,0-0:42.0.0.255,2} (LDN)
        "000100100001000dc001c1000100002a0000ff0200",
        # 11. Corrupted client/server addresses (two bits flip)
        "000100140002000dc001c100010000000200ff0200",
        # 12. Corrupted client/server addresses (two bits flip)
        "000100150002000dc001c100010000000200ff0200",
        # 13. RLRQ
        "00010010000100026200",
        # 14. AARQ: AA={16,1}, No-Ciphering,No-Auth
        "0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000",
        # 15. Get: {1,0-0:42.0.0.255,2} (LDN)
        "000100100001000dc001c1000100002a0000ff0200",
        # 16. Corrupted client/server addresses (two bits flip)
        "000100160002000dc001c100010000000200ff0200",
        # 17. RLRQ
        "00010010000100026200",
        # 18. AARQ: AA={16,1}, No-Ciphering,No-Auth
        "0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000",
        # 19. Get: {1,0-0:42.0.0.255,2} (LDN)
        "000100100001000dc001c1000100002a0000ff0200",
        # 20. Corrupted client/server addresses (two bits flip)
        "000100170002000dc001c100010000000200ff0200",
        # 21. RLRQ
        "00010010000100026200",
        # 22. AARQ: AA={16,1}, No-Ciphering,No-Auth, corrupted client/server addresses.
        #     After this step, the meter's remote channel DLMS must die, being not able
        #     to talk anymore.
        "0001001800020028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000"
    ]

    forever_halt_2 = [
        # 00. AARQ: AA={16,1}, No-Ciphering,No-Auth
        "0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000",
        # 01. Get: {1,0-0:42.0.0.255,2} (LDN)
        "000100100001000dc001c0000100002a0000ff0200",
        # 02. RLRQ
        "00010010000100026200",
        # 03. AARQ: AA={16,1}, No-Ciphering,No-Auth
        "0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000",
        # 04. Get: {1,0-0:42.0.0.255,2} (LDN), one bit flip in the payload (offset 10):
        # 'c0' -> '80'
        "000100100001000dc001 80 000100002a0000ff0200",
        # 05. RLRQ
        # This will fail, no response
        "00010010000100026200",
        # 06. AARQ: AA={16,1}, No-Ciphering,No-Auth
        # This will also fail, no response.
        "0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000"
    ]

    simple_and_normal = [
        # 00. AARQ: AA={16,1}, No-Ciphering,No-Auth
        "0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000",
        # 01. Get: {1,0-0:42.0.0.255,2} (LDN)
        "000100100001000dc001c1000100002a0000ff0200",
        # 02. RLRQ
        "00010010000100026200"
    ]

    temp_halt_01 = [
        # 00. AARQ: AA={16,1}, No-Ciphering,No-Auth
        "0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000",
        # 01. Get: {1,0-0:42.0.0.255,2} (LDN)
        "000100100001000dc001c1000100002a0000ff0200",
        # 02. RLRQ
        "00010010000100026200",
        # 03. AARQ: AA={16,1}, No-Ciphering,No-Auth
        "00010010000100286026 80 020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000",
        # 04. Get: {1,0-0:42.0.0.255,2} (LDN), one bit error in WPDU version field
        # (offset 1).
        # This actually will the message being dropped by the link layer,
        # it will not be seen by the DLMS server.
        "010100100001000dc001c1000100002a0000ff0200",
        # 05. RLRQ.
        # This will timeout due to an ACSE bug
        "00010010000100026200",
        # 06. AARQ: AA={16,1}, No-Ciphering,No-Auth.  This also timeout. At this point,
        # the client can neight release nor establish the AA. The halted communication
        # can only be recovered after the DLMS InactivityTimeout time.
        "0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000"
    ]

    temp_halt_02 = [
        # 00. AARQ: AA={16,1}, No-Ciphering,No-Auth
        "0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000",
        # 01. Get: {1,0-0:42.0.0.255,2} (LDN)
        "000100100001000dc001c1000100002a0000ff0200",
        # 02. RLRQ
        "00010010000100026200",
        # 03. AARQ: AA={16,1}, No-Ciphering,No-Auth
        "00010010000100286026 80 020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000",
        # 04. RLRQ.
        # This will timeout due to an ACSE bug
        "00010010000100026200",
        # 05. AARQ: AA={16,1}, No-Ciphering,No-Auth.  This also timeout. At this point,
        # the client can neight release nor establish the AA. The halted communication
        # can only be recovered after the DLMS InactivityTimeout time.
        "0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000"
    ]

    HC1_tcp_pool_exhaust = [
        # 01. AARQ: AA={16,1}, No-Ciphering,No-Auth
        "0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000",
        # 01. Get: {1,0-0:42.0.0.255,2} (LDN)
        "000100100001000dc001c1000100002a0000ff0200",
        # 02. Corrupted client/server addresses (two bits flip)
        "000100110002000dc001c100010000000200ff0200",
        # 03. RLRQ
        "00010010000100026200",
        # 04. AARQ: AA={16,1}, No-Ciphering,No-Auth
        "0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000",
        # 05. Get: {1,0-0:42.0.0.255,2} (LDN)
        "000100100001000dc001c1000100002a0000ff0200",
        # 06. Zero-length payload; corrupted client address
        "0001001200010000",
        # 07. RLRQ
        "00010010000100026200",
        # 08. None-DLMS but a valid WPDU; Corrupted client/server addresses (two bits
        # flip)
        "000100130002000a00010203040506070809",
        # 09. AARQ: AA={16,1}, No-Ciphering,No-Auth
        "0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000",
        # 10. Get: {1,0-0:42.0.0.255,2} (LDN)
        "000100100001000dc001c1000100002a0000ff0200",
        # 11. Corrupted client/server addresses (two bits flip)
        "000100140002000dc001c100010000000200ff0200",
        # 12. Corrupted client/server addresses (two bits flip)
        "000100150002000dc001c100010000000200ff0200",
        # 13. RLRQ
        "00010010000100026200",
        # 14. AARQ: AA={16,1}, No-Ciphering,No-Auth
        "0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000",
        # 15. Get: {1,0-0:42.0.0.255,2} (LDN)
        "000100100001000dc001c1000100002a0000ff0200",
        # 16. Corrupted client/server addresses (two bits flip)
        "000100160002000dc001c100010000000200ff0200",
        # 17. RLRQ
        "00010010000100026200",
        # 18. AARQ: AA={16,1}, No-Ciphering,No-Auth
        "0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000",
        # 19. Get: {1,0-0:42.0.0.255,2} (LDN)
        "000100100001000dc001c1000100002a0000ff0200",
        # 20. Corrupted client/server addresses (two bits flip)
        "000100170002000dc001c100010000000200ff0200",
        # 21. RLRQ
        "00010010000100026200",
        # 22. AARQ: AA={16,1}, No-Ciphering,No-Auth, corrupted client/server addresses.
        #     After this step, the meter's remote channel DLMS must die, being not able
        #     to talk anymore.
        "0001001800020028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000"
    ]

    HC2_no_RLRQ_response = [
        # 01. AARQ: AA={16,1}, No-Ciphering,No-Auth
        "0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000",
        # 01. Get: {1,0-0:42.0.0.255,2} (LDN)
        "000100100001000dc001c1000100002a0000ff0200",
        # 02. RLRQ
        "00010010000100026200",
        # 03. AARQ: AA={16,1}, No-Ciphering,No-Auth
        "0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000",
        # 04. RLRQ.
        # This will timeout due to an ACSE bug
        "00010010000100026200",
        # 05. AARQ: AA={16,1}, No-Ciphering,No-Auth.  This also timeout. At this point,
        # the client can neight release nor establish the AA. The halted communication
        # can only be recovered after the DLMS InactivityTimeout time.
        "0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000",
    ]

    HC3_parse_zero_length = [
        # 00. AARQ: AA={16,1}, No-Ciphering,No-Auth
        "0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000",
        # 01. Get: {1,0-0:42.0.0.255,2} (LDN)
        "000100100001000dc001c0000100002a0000ff0200",
        # 02. RLRQ
        "00010010000100026200",
        # 03. AARQ: AA={16,1}, No-Ciphering,No-Auth
        "0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000",
        # 04. Get: {1,0-0:42.0.0.255,2} (LDN), one bit flip in the payload (offset 10):
        # 'c0' -> '80'
        "000100100001000dc00180000100002a0000ff0200",
        # 05. RLRQ
        # This will fail, no response
        "00010010000100026200",
        # 06. AARQ: AA={16,1}, No-Ciphering,No-Auth
        # This will also fail, no response.
        "0001001000010028602680020780a109060760857405080101a903020101be10040e01000000065f1f040000f2df0000"
    ]

    def __init__(self):
        pass