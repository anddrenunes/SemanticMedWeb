xquery version "3.0";
declare namespace mlhim2="http://www.mlhim.org/xmlns/mlhim2/2_4_1";
let $title := "By Gender Counts"
let $demogs := collection("/db/apps/mlhim-emr/data/demog")//mlhim2:el-06b0c425-f7ef-4d46-8573-97091ae52d60
  let $total := count($demogs)
  let $mcnt := count($demogs//mlhim2:el-0ac3f22e-64ca-4309-be88-874cd14649a0[contains(mlhim2:DvString-dv,"Male")])
  let $fcnt := count($demogs//mlhim2:el-0ac3f22e-64ca-4309-be88-874cd14649a0[contains(mlhim2:DvString-dv,"Female")])

return
      <results>
      <ReportTitle>{$title}</ReportTitle>
      <male>{$mcnt}</male>
      <female>{$fcnt}</female>
      <Total>{$total}</Total>
      </results>