# use in merge request, default repos
import json
import os

from merico.diff_pipeline.constants import CUSTOM_REPOS
from merico.diff_pipeline.schemas import Repo

MINI_REPOS = [
    Repo(
        url="https://github.com/microsoft/FASTER.git",
        hexsha="a31b52b29e952827b4ad464674df57d9e230020a",
    ),
    Repo(
        url="https://github.com/docker-library/python.git",
        hexsha="4bff010c9735707699dd72524c7d1a827f6f5933",
    ),
    Repo(
        url="https://github.com/json-iterator/java.git",
        hexsha="e48a7a1958f5f99ceb2a419d88e92131843388b1",
    ),
    Repo(
        url="https://github.com/jeffheaton/encog-c.git",
        hexsha="d207819b86d1c2b4dba114dbc3cbd784df999e05",
    ),
    Repo(
        url="https://github.com/golang/oauth2.git",
        hexsha="5e61552d6c78ccf28c6977693409db7f86c17379",
    ),
    Repo(
        url="https://github.com/julianshapiro/velocity.git",
        hexsha="767e35cac12120be526eef330e4d988b2c3cfc3c",
    ),
    Repo(
        url="https://github.com/google/glog.git",
        hexsha="8d40d7564d4a06d77d707d7c4a50c8b5dc45dd80",
    ),
    Repo(
        url="https://github.com/rbenv/rbenv.git",
        hexsha="d604acb78aeba583be95f08d45eeae430372beb9",
    ),
    Repo(
        url="https://github.com/NMAC427/SwiftOCR.git",
        hexsha="99a1d90a5f3ddef51492bca8f6606f2a60e18ffe",
    ),
    Repo(
        url="https://github.com/Kotlin/kotlinx.serialization.git",
        hexsha="daa95c79ffadc0eedbbb4a481a00556b78212e43",
    ),
    Repo(
        url="https://github.com/RustScan/RustScan.git",
        hexsha="30856350d36ba44b73c239d44f6dc17c0e69879b",
    ),
    Repo(
        url="https://github.com/jwtk/jjwt.git",
        hexsha="a4130dd1ec5d4bef4b1835927a2a1d966a519109",
    ),
    Repo(
        url="https://github.com/ccgus/fmdb.git",
        hexsha="5644ee43eeed786824eaaa77550d23d82eaa7723",
    ),
    Repo(
        url="https://github.com/vlucas/phpdotenv.git",
        hexsha="b3eac5c7ac896e52deab4a99068e3f4ab12d9e56",
    ),
    Repo(
        url="https://github.com/scalatron/scalatron.git",
        hexsha="7c3b6b9725a33ddcf0da78aebb3844e91fa42ebe",
    ),
    Repo(
        url="https://github.com/vincentzyc/vue3-demo.git",
        hexsha="1c37a7b9fb0c28dc08ebea9bbdcee21a6e44479e",
    ),
    Repo(
        url="https://github.com/dart-lang/markdown.git",
        hexsha="d72ae07c8290b3780044170eda28eda5a9fb342e",
    ),
    Repo(
        url="https://github.com/oldboyxx/jira_clone.git",
        hexsha="26a9e77b1789fef9cb43edb5d6018cf1663cf035",
    ),
    Repo(
        url="https://github.com/jmschrei/pomegranate.git",
        hexsha="0652e955c400bc56df5661db3298a06854c7cce8",
    ),
    Repo(
        url="https://github.com/supabase/pg_graphql.git",
        hexsha="dac12787e3681eeedc6be02cc56d26d7550208d9",
    ),
    Repo(
        url="https://github.com/LunarVim/LunarVim.git",
        hexsha="09cbce44e54976a809c941a71579d7b3b4862b4e",
    ),
]
# use in commit, small repo
FAST_REPOS = [
    Repo(
        url="https://github.com/mkj/dropbear.git",
        hexsha="9262ffe8617bd8d631edf30772650ff4d5d156c6",
    ),
    Repo(
        url="https://github.com/tiangolo/fastapi.git",
        hexsha="c09e950bd2efb81f82931469bee6856c72e54357",
    ),
    Repo(
        url="https://github.com/ccgus/fmdb.git",
        hexsha="3e5efdf6690cf7dce0a914c370507deee8740d33",
    ),
    Repo(
        url="https://github.com/gliderlabs/ssh.git",
        hexsha="30ec06db4e743ac9f827a69c8b8cfb84064a6dc7",
    ),
    Repo(
        url="https://github.com/alibaba/arthas.git",
        hexsha="f19bd33805f752ffefcf1e6a914a24a5e0141e9a",
    ),
    Repo(
        url="https://github.com/t4t5/sweetalert.git",
        hexsha="82c8869761c138f1fba7771a818e40f1aab35be6",
    ),
    Repo(
        url="https://github.com/rbenv/rbenv.git",
        hexsha="d604acb78aeba583be95f08d45eeae430372beb9",
    ),
    Repo(
        url="https://github.com/ZupIT/horusec.git",
        hexsha="60bef4ba368da49fcdad7104000a3026989692ba",
    ),
    Repo(
        url="https://github.com/InsertKoinIO/koin.git",
        hexsha="9e3e14cf4b7a952bb104754348e39c085b03f5c7",
    ),
    Repo(
        url="https://github.com/yahoo/CMAK.git",
        hexsha="8e16403c65009280ae30e9fd1b2bfc0dcdd7d714",
    ),
    Repo(
        url="https://github.com/sharkdp/fd.git",
        hexsha="f60b7687a2f189dfc4009b23e5af6b6049dbd1b5",
    ),
    Repo(
        url="https://github.com/xmartlabs/Eureka.git",
        hexsha="f9c96ab5a13ba42f6566d6e18ab38610c25a72ad",
    ),
    Repo(
        url="https://github.com/bchavez/Bogus.git",
        hexsha="b9049abf8b40203c09079741bcb328da95899f81",
    ),
    Repo(
        url="https://github.com/vlucas/phpdotenv.git",
        hexsha="b3eac5c7ac896e52deab4a99068e3f4ab12d9e56",
    ),
    Repo(
        url="https://github.com/microsoft/calculator.git",
        hexsha="5cf27f1fe16408273945ccdb12d838cab9202f0e",
    ),
    Repo(
        url="https://github.com/hellokoding/registration-login-spring-hsql.git",
        hexsha="e514e2565c2b76b4aa444430b1dd60baf5863c3c",
    ),
    Repo(
        url="https://github.com/lerna/lerna.git",
        hexsha="6cb8ab2d4af7ce25c812e8fb05cd04650105705f",
    ),
    Repo(
        url="https://github.com/vue-generators/vue-form-generator.git",
        hexsha="721a4eebbde77040a1318e60aa9ef21229bbcf99",
    ),
    Repo(
        url="https://github.com/yamafaktory/shrimpit.git",
        hexsha="64866939edf724f0aacd2fb39373241fe36d03b6",
    ),
    Repo(
        url="https://github.com/oldboyxx/jira_clone.git",
        hexsha="26a9e77b1789fef9cb43edb5d6018cf1663cf035",
    ),
    Repo(
        url="https://github.com/jmschrei/pomegranate.git",
        hexsha="0652e955c400bc56df5661db3298a06854c7cce8",
    ),
    Repo(
        url="https://github.com/supabase/pg_graphql.git",
        hexsha="dac12787e3681eeedc6be02cc56d26d7550208d9",
    ),
    Repo(
        url="https://github.com/LunarVim/LunarVim.git",
        hexsha="09cbce44e54976a809c941a71579d7b3b4862b4e",
    ),
]


def get_repos_from_env():
    repos_str = os.getenv(CUSTOM_REPOS)
    if repos_str:
        repos_list = json.loads(repos_str)
        repos = []
        for item in repos_list:
            repos.append(Repo.parse_obj(item))
    else:
        repos = MINI_REPOS if os.getenv("CI_MERGE_REQUEST_IID") else FAST_REPOS
    return repos
