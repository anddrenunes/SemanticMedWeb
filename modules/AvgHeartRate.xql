xquery version "3.0";
declare namespace mlhim2="http://www.mlhim.org/xmlns/mlhim2/2_4_1";
let $hr := collection("/db/apps/mlhim-emr/data/care")//mlhim2:el-02555aa1-5e33-4dc3-9da6-e592839db930/mlhim2:magnitude
  return <heart-rate-average>{avg($hr)}</heart-rate-average>