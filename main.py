from ai5win_mes_gui import AI5WINMesGUI

debug = False


def test(mode: str):
    # diss, ass, diss_for_hack, spec_cmp...
    from ai5win_mes import AI5WINScript

    base_name = "S67SE"
    script_mes = "{}.MES".format(base_name)
    file_txt = "{}.txt".format(base_name)

    if mode == "diss":
        new_script = AI5WINScript(script_mes, file_txt, version=1, verbose=True, debug=False)
        new_script.disassemble()
        del new_script
    elif mode == "ass":
        new_script = AI5WINScript(script_mes, file_txt, version=1, verbose=True, debug=False)
        new_script.assemble()
        del new_script
    elif mode == "diss_for_hack":
        new_script = AI5WINScript(script_mes, file_txt, version=1, verbose=True, debug=True, hackerman_mode=True)
        new_script.disassemble()
        del new_script


def main():
    gui = AI5WINMesGUI()
    return True


if __name__ == '__main__':
    if debug:
        test("diss")
    else:
        main()
