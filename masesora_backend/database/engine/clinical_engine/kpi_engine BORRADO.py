def compute_kpi(short_code: str, input_a: float, input_b: float) -> float | None:
    if input_a is None or input_b is None:
        return None

    match short_code:

        # -------------------------
        # UCI
        # -------------------------
        case "UCI-S1":
            if input_b == 0:
                return None
            return input_a / (input_b / 30)

        case "UCI-S2":
            if input_a == 0:
                return None
            return (input_a - input_b) / input_a

        case "UCI-S3":
            if input_a == 0:
                return None
            return (input_a - input_b) / input_a

        case "UCI-S4":
            if input_b == 0:
                return None
            return input_a / input_b

        case "UCI-S5":
            if input_b == 0:
                return None
            return input_a / input_b

        case "UCI-S6":
            if input_b == 0:
                return None
            return input_a / input_b

        case "UCI-S7":
            if input_b == 0:
                return None
            return input_a / input_b

        case "UCI-S8":
            if input_b == 0:
                return None
            return input_a / input_b

        case "UCI-S9":
            if input_b == 0:
                return None
            return (input_b - input_a) / input_a

        case "UCI-S10":
            if input_b == 0:
                return None
            return input_a / input_b


        # -------------------------
        # UNI
        # -------------------------
        case "UNI-S1":
            if input_a == 0:
                return None
            return input_b / input_a

        case "UNI-S2":
            if input_a == 0:
                return None
            return input_b / input_a

        case "UNI-S3":
            if input_a == 0:
                return None
            return input_a / input_b

        case "UNI-S4":
            if input_b == 0:
                return None
            return input_a / input_b

        case "UNI-S5":
            if input_b == 0:
                return None
            return input_a / input_b

        case "UNI-S6":
            if input_a == 0:
                return None
            return input_b / input_a

        case "UNI-S7":
            if input_b == 0:
                return None
            return input_a / input_b

        case "UNI-S8":
            if input_a == 0:
                return None
            return input_b / input_a

        case "UNI-S9":
            if input_b == 0:
                return None
            return input_a / input_b

        case "UNI-S10":
            if input_b == 0:
                return None
            return input_a / input_b


        # -------------------------
        # CARDIO
        # -------------------------
        case "CARDIO-S1":
            if input_a == 0:
                return None
            return (input_b / input_a) * 100

        case "CARDIO-S2":
            if input_b == 0:
                return None
            return (input_a / input_b) * 100

        case "CARDIO-S3":
            if input_a == 0:
                return None
            return input_b / input_a

        case "CARDIO-S4":
            if input_b == 0:
                return None
            return input_a / input_b

        case "CARDIO-S5":
            if input_b == 0:
                return None
            return (input_a / input_b) * 100

        case "CARDIO-S6":
            if input_b == 0:
                return None
            return (input_a / input_b) * 100

        case "CARDIO-S7":
            if input_b == 0:
                return None
            return input_a / input_b

        case "CARDIO-S8":
            return input_b - input_a

        case "CARDIO-S9":
            if input_a == 0:
                return None
            return (input_b / input_a) * 100

        case "CARDIO-S10":
            if input_b == 0:
                return None
            return (input_a / input_b) * 100


        # -------------------------
        # NEURO
        # -------------------------
        case "NEURO-S1":
            if input_b == 0:
                return None
            return input_a / input_b

        case "NEURO-S2":
            if input_b == 0:
                return None
            return input_a / input_b

        case "NEURO-S3":
            if input_b == 0:
                return None
            return input_a / input_b

        case "NEURO-S4":
            if input_b == 0:
                return None
            return input_a / input_b

        case "NEURO-S5":
            if input_b == 0:
                return None
            return input_a / input_b

        case "NEURO-S6":
            if input_b == 0:
                return None
            return input_a / input_b

        case "NEURO-S7":
            if input_b == 0:
                return None
            return input_a / input_b

        case "NEURO-S8":
            if input_b == 0:
                return None
            return input_a / input_b

        case "NEURO-S9":
            if input_b == 0:
                return None
            return (1 / input_b) * input_a

        case "NEURO-S10":
            if input_b == 0:
                return None
            return input_a / input_b


        # -------------------------
        # CLI
        # -------------------------
        case "CLI-S1":
            return input_a - input_b

        case "CLI-S2":
            if input_b == 0:
                return None
            return input_a / input_b

        case "CLI-S3":
            if input_b == 0:
                return None
            return input_a / input_b

        case "CLI-S4":
            if input_b == 0:
                return None
            return input_a / input_b

        case "CLI-S5":
            if input_b == 0:
                return None
            return input_a / input_b

        case "CLI-S6":
            if input_b == 0:
                return None
            return input_a / input_b

        case "CLI-S7":
            if input_b == 0:
                return None
            return input_a / input_b

        case "CLI-S8":
            if input_b == 0:
                return None
            return input_a / input_b

        case "CLI-S9":
            if input_b == 0:
                return None
            return input_a / input_b

        case "CLI-S10":
            if input_b == 0:
                return None
            return input_a / input_b


        # -------------------------
        # CIR
        # -------------------------
        case "CIR-S1":
            if input_b == 0:
                return None
            return input_a / input_b

        case "CIR-S2":
            if input_b == 0:
                return None
            return input_a / input_b

        case "CIR-S3":
            if input_b == 0:
                return None
            return input_a / input_b

        case "CIR-S4":
            if input_b == 0:
                return None
            return input_a / input_b

        case "CIR-S5":
            if input_b == 0:
                return None
            return input_a / input_b

        case "CIR-S6":
            if input_b == 0:
                return None
            return input_a / input_b

        case "CIR-S7":
            if input_b == 0:
                return None
            return input_a / input_b

        case "CIR-S8":
            if input_b == 0:
                return None
            return input_a / input_b

        case "CIR-S9":
            if input_b == 0:
                return None
            return input_a / input_b

        case "CIR-S10":
            if input_b == 0:
                return None
            return input_a / input_b


        # -------------------------
        # PSI
        # -------------------------
        case "PSI-S1":
            if input_b == 0:
                return None
            return input_a / input_b

        case "PSI-S2":
            if input_b == 0:
                return None
            return input_a / input_b

        case "PSI-S3":
            if input_b == 0:
                return None
            return input_a / input_b

        case "PSI-S4":
            if input_b == 0:
                return None
            return input_a / input_b

        case "PSI-S5":
            if input_b == 0:
                return None
            return input_a / input_b

        case "PSI-S6":
            if input_b == 0:
                return None
            return input_a / input_b

        case "PSI-S7":
            if input_b == 0:
                return None
            return input_a / input_b

        case "PSI-S8":
            if input_b == 0:
                return None
            return input_a / input_b

        case "PSI-S9":
            if input_b == 0:
                return None
            return input_a / input_b

        case "PSI-S10":
            if input_b == 0:
                return None
            return input_a / input_b


        # -------------------------
        # RES
        # -------------------------
        case "RES-S1":
            if input_b == 0:
                return None
            return input_a / input_b

        case "RES-S2":
            if input_b == 0:
                return None
            return input_a / input_b

        case "RES-S3":
            if input_b == 0:
                return None
            return input_a / input_b

        case "RES-S4":
            if input_b == 0:
                return None
            return input_a / input_b

        case "RES-S5":
            if input_b == 0:
                return None
            return input_a / input_b

        case "RES-S6":
            if input_b == 0:
                return None
            return input_a / input_b

        case "RES-S7":
            if input_b == 0:
                return None
            return input_a / input_b

        case "RES-S8":
            if input_b == 0:
                return None
            return input_a / input_b

        case "RES-S9":
            if input_b == 0:
                return None
            return input_a / input_b

        case "RES-S10":
            if input_b == 0:
                return None
            return input_a / input_b


        # -------------------------
        # OPE
        # -------------------------
        case "OPE-S1":
            if input_b == 0:
                return None
            return input_a / input_b

        case "OPE-S2":
            if input_b == 0:
                return None
            return input_a / input_b

        case "OPE-S3":
            if input_b == 0:
                return None
            return input_a / input_b

        case "OPE-S4":
            if input_b == 0:
                return None
            return input_a / input_b

        case "OPE-S5":
            if input_b == 0:
                return None
            return input_a / input_b

        case "OPE-S6":
            if input_b == 0:
                return None
            return input_a / input_b

        case "OPE-S7":
            if input_b == 0:
                return None
            return input_a / input_b

        case "OPE-S8":
            if input_b == 0:
                return None
            return input_a / input_b

        case "OPE-S9":
            if input_b == 0:
                return None
            return input_a / input_b

        case "OPE-S10":
            if input_b == 0:
                return None
            return input_a / input_b
        # -------------------------
        # TER
        # -------------------------
        case "TER-S2":
            if input_b == 0:
                return None
            return (input_a / input_b) * 100

        case "TER-S3":
            if input_b == 0:
                return None
            return (input_a / input_b) * 100

        case "TER-S4":
            if input_b == 0:
                return None
            return (input_a / input_b) * 100

        case "TER-S5":
            if input_b == 0:
                return None
            return (input_a / input_b) * 100

        case "TER-S6":
            if input_b == 0:
                return None
            return (input_a / input_b) * 100

        case "TER-S7":
            return input_a - input_b

        case "TER-S8":
            if input_b == 0:
                return None
            return (input_a / input_b) * 100

        case "TER-S9":
            if input_b == 0:
                return None
            return input_a / input_b

        case "TER-S10":
            if input_b == 0:
                return None
            return (input_a / input_b) * 100


        # -------------------------
        # OPE
        # -------------------------
        case "OPE-S1":
            if input_b == 0:
                return None
            return input_a / input_b

        case "OPE-S2":
            if input_b == 0:
                return None
            return input_a / input_b

        case "OPE-S3":
            if input_b == 0:
                return None
            return input_a / input_b

        case "OPE-S4":
            if input_b == 0:
                return None
            return input_a / input_b

        case "OPE-S5":
            if input_b == 0:
                return None
            return input_a / input_b

        case "OPE-S6":
            if input_b == 0:
                return None
            return input_a / input_b

        case "OPE-S7":
            if input_b == 0:
                return None
            return input_a / input_b

        case "OPE-S8":
            if input_b == 0:
                return None
            return input_a / input_b

        case "OPE-S9":
            if input_b == 0:
                return None
            return input_a / input_b

        case "OPE-S10":
            if input_b == 0:
                return None
            return input_a / input_b


        # -------------------------
        # DEFAULT
        # -------------------------
        case _:
            return None

       