DROP_TBL_PERFDATA = "DROP TABLE perfdata"

CREATE_TBL_PERFDATA = """CREATE TABLE `perfdata` (
  `pk` int(11) NOT NULL AUTO_INCREMENT,
  `id` varchar(16) NOT NULL,
  `fn` varchar(256) NOT NULL,
  `wt` int(11) NOT NULL,
  `ct` int(11) NOT NULL,
  `pmu` int(11) NOT NULL,
  `mu` int(11) NOT NULL,
  `cpu` int(11) NOT NULL,
  `rec_on` datetime NOT NULL,
  PRIMARY KEY (`pk`)
)"""

CREATE_TBL_PARENT_CHILD = """CREATE TABLE IF NOT EXISTS `parent_child` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `run` varchar(32) NOT NULL,
  `parent` varchar(128) DEFAULT NULL,
  `child` varchar(128) NOT NULL,
  `wt` int(11) NOT NULL,
  `pmu` int(11) NOT NULL,
  `mu` int(11) NOT NULL,
  `cpu` int(11) NOT NULL,
  `ct` int(11) NOT NULL,
  `rec_on` datetime NOT NULL,
  PRIMARY KEY (`id`)
)""";

SELECT_DETAILS = "select id, get, post, cookie, perfdata, `timestamp` from details"

INSERT_INTO_PC = """insert into parent_child (run, parent, child, ct, wt, cpu, mu, pmu, rec_on) values
        (
        %(run_id)s,
        %(parent)s,
        %(child)s,
        %(callnum)s,
        %(walltime)s,
        %(proc)s,
        %(mem)s,
        %(peakmem)s,
        %(rec_on)s
        )""";
