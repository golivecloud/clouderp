#!/usr/bin/env python
#----------------------------------------------------------
# clouderp cli
#
# To install your clouderp development environement type:
#
# wget -O- https://raw.githubusercontent.com/clouderp/clouderp/9.0/clouderp.py | python
#
# The setup_* subcommands used to boostrap clouderp are defined here inline and may
# only depends on the python 2.7 stdlib
#
# The rest of subcommands are defined in clouderp/cli or in <module>/cli by
# subclassing the Command object
#
#----------------------------------------------------------
import os
import re
import sys
import subprocess

GIT_HOOKS_PRE_PUSH = """
#!/usr/bin/env python2
import re
import sys
if re.search('github.com[:/]clouderp/clouderp.git$', sys.argv[2]):
    print "Pushing to /clouderp/clouderp.git is forbidden, please push to clouderp-dev, use --no-verify to override"
    sys.exit(1)
"""

def printf(f,*l):
    print "clouderp:" + f % l

def run(*l):
    if isinstance(l[0], list):
        l = l[0]
    printf("running %s", " ".join(l))
    subprocess.check_call(l)

def git_locate():
    # Locate git dir
    # TODO add support for os.environ.get('GIT_DIR')

    # check for an clouderp child
    if os.path.isfile('clouderp/.git/config'):
        os.chdir('clouderp')

    path = os.getcwd()
    while path != os.path.abspath(os.sep):
        gitconfig_path = os.path.join(path, '.git/config')
        if os.path.isfile(gitconfig_path):
            release_py = os.path.join(path, 'gce/release.py')
            if os.path.isfile(release_py):
                break
        path = os.path.dirname(path)
    if path == os.path.abspath(os.sep):
        path = None
    return path

def cmd_setup_git():
    git_dir = git_locate()
    if git_dir:
        printf('git repo found at %s',git_dir)
    else:
        run("git", "init", "clouderp")
        os.chdir('clouderp')
        git_dir = os.getcwd()
    if git_dir:
        # push sane config for git < 2.0, and hooks
        #run('git','config','push.default','simple')
        # alias
        run('git','config','alias.st','status')
        # merge bzr style
        run('git','config','merge.commit','no')
        # pull let me choose between merge or rebase only works in git > 2.0, use an alias for 1
        run('git','config','pull.ff','only')
        run('git','config','alias.pl','pull --ff-only')
        pre_push_path = os.path.join(git_dir, '.git/hooks/pre-push')
        open(pre_push_path,'w').write(GIT_HOOKS_PRE_PUSH.strip())
        os.chmod(pre_push_path, 0755)
        # setup clouderp remote
        run('git','config','remote.clouderp.url','https://github.com/golivecloud/clouderp.git')
        run('git','config','remote.clouderp.pushurl','git@github.com:clouderp/clouderp.git')
        run('git','config','--add','remote.clouderp.fetch','dummy')
        run('git','config','--unset-all','remote.clouderp.fetch')
        run('git','config','--add','remote.clouderp.fetch','+refs/heads/*:refs/remotes/clouderp/*')
        # setup clouderp-dev remote
        run('git','config','remote.clouderp-dev.url','https://github.com/golivecloud-dev/clouderp.git')
        run('git','config','remote.clouderp-dev.pushurl','git@github.com:clouderp-dev/clouderp.git')
        run('git','remote','update')
        # setup 9.0 branch
        run('git','config','branch.9.0.remote','clouderp')
        run('git','config','branch.9.0.merge','refs/heads/9.0')
        run('git','checkout','9.0')
    else:
        printf('no git repo found')

def cmd_setup_git_dev():
    git_dir = git_locate()
    if git_dir:
        # setup clouderp-dev remote
        run('git','config','--add','remote.clouderp-dev.fetch','dummy')
        run('git','config','--unset-all','remote.clouderp-dev.fetch')
        run('git','config','--add','remote.clouderp-dev.fetch','+refs/heads/*:refs/remotes/clouderp-dev/*')
        run('git','config','--add','remote.clouderp-dev.fetch','+refs/pull/*:refs/remotes/clouderp-dev/pull/*')
        run('git','remote','update')

def cmd_setup_git_review():
    git_dir = git_locate()
    if git_dir:
        # setup clouderp-dev remote
        run('git','config','--add','remote.clouderp.fetch','dummy')
        run('git','config','--unset-all','remote.clouderp.fetch')
        run('git','config','--add','remote.clouderp.fetch','+refs/heads/*:refs/remotes/clouderp/*')
        run('git','config','--add','remote.clouderp.fetch','+refs/tags/*:refs/remotes/clouderp/tags/*')
        run('git','config','--add','remote.clouderp.fetch','+refs/pull/*:refs/remotes/clouderp/pull/*')

def setup_deps_debian(git_dir):
    debian_control_path = os.path.join(git_dir, 'debian/control')
    debian_control = open(debian_control_path).read()
    debs = re.findall('python-[0-9a-z]+',debian_control)
    debs += ["postgresql"]
    proc = subprocess.Popen(['sudo','apt-get','install'] + debs, stdin=open('/dev/tty'))
    proc.communicate()

def cmd_setup_deps():
    git_dir = git_locate()
    if git_dir:
        if os.path.isfile('/etc/debian_version'):
            setup_deps_debian(git_dir)

def setup_pg_debian(git_dir):
    cmd = ['sudo','su','-','postgres','-c','createuser -s %s' % os.environ['USER']]
    subprocess.call(cmd)

def cmd_setup_pg():
    git_dir = git_locate()
    if git_dir:
        if os.path.isfile('/etc/debian_version'):
            setup_pg_debian(git_dir)

def cmd_setup():
    cmd_setup_git()
    cmd_setup_deps()
    cmd_setup_pg()

def main():
    # registry of commands
    g = globals()
    cmds = dict([(i[4:],g[i]) for i in g if i.startswith('cmd_')])
    # if curl URL | python2 then use command setup
    if len(sys.argv) == 1 and __file__ == '<stdin>':
        cmd_setup()
    elif len(sys.argv) == 2 and sys.argv[1] in cmds:
        cmds[sys.argv[1]]()
    else:
        import gce
        gce.cli.main()

if __name__ == "__main__":
    main()
