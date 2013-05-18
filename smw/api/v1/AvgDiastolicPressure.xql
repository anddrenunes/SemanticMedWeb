xquery version "3.0";
declare namespace mlhim2="http://www.mlhim.org/xmlns/mlhim2/2_4_1";
let $sp := collection("/db/apps/mlhim-emr/data/care")//mlhim2:el-3ad51caa-b762-42a8-a284-96707d37240b/mlhim2:magnitude
  return <systolic-average>{avg($sp)}</systolic-average>