from rpython.jit.codewriter.policy import JitPolicy

from r12a.main import create_entry_point


def target(driver, args):
    driver.exe_name = "bin/r12a"
    #driver.config.set(**get_topaz_config_options())
    return create_entry_point(driver.config), None


def jitpolicy(driver):
    return JitPolicy()


def handle_config(config, translateconfig):
    #config.translation.suggest(check_str_without_nul=True)
    pass
