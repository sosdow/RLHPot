create table `commands` (
    `id`	 int(11) NOT NULL auto_increment,
    `command` char(32) NOT NULL,
    `impl_type` int(4) NOT NULL,
    `prof_type` char(32) NOT NULL,
    	PRIMARY KEY (`id`)
);

create table fake_commands(
    `id`	 int(11) NOT NULL auto_increment,
    `command` char(32) NOT NULL,
    `fake_output` char(32) NOT NULL,
    	PRIMARY KEY (`id`)
);

create table cases(
    `id`	 int(11) NOT NULL auto_increment,
    `initial_cmd` char(32) NOT NULL,
    `cmd_profile` char(32) NOT NULL,
    `action` int(4) NOT NULL,
    `action_param` char(32) NOT NULL,
    `rl_params` char(32) NOT NULL,
    `next_cmd` char(32) NOT NULL,
    	PRIMARY KEY (`id`)
);