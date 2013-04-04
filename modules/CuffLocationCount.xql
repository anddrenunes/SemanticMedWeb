xquery version "3.0";
declare namespace mlhim2="http://www.mlhim.org/xmlns/mlhim2/2_4_1";
let $title := "BP Cuff Location Counts"
let $vitals := collection("/db/apps/mlhim-emr/data/care")//mlhim2:el-a2bc25db-3111-4cd5-9825-d9c448cdd1a4
  let $total := count($vitals)
  let $uarcnt := count($vitals//mlhim2:el-248f086e-f98c-432c-a38b-e8aa4710b4dc[contains(mlhim2:DvString-dv,"Upper Arm, Right")])
  let $ualcnt := count($vitals//mlhim2:el-248f086e-f98c-432c-a38b-e8aa4710b4dc[contains(mlhim2:DvString-dv,"Upper Arm, Left")])
  let $wrcnt := count($vitals//mlhim2:el-248f086e-f98c-432c-a38b-e8aa4710b4dc[contains(mlhim2:DvString-dv,"Wrist, Right")])
  let $wlcnt := count($vitals//mlhim2:el-248f086e-f98c-432c-a38b-e8aa4710b4dc[contains(mlhim2:DvString-dv,"Wrist, Left")])

return
      <results>
      <ReportTitle>{$title}</ReportTitle>
      <upper-arm-right>{$uarcnt}</upper-arm-right>
      <upper-arm-left>{$ualcnt}</upper-arm-left>
      <wrist-right>{$wrcnt}</wrist-right>
      <wrist-left>{$wrcnt}</wrist-left>
      <Total>{$total}</Total>
      </results>