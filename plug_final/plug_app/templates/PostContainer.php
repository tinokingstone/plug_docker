<!DOCTYPE html>
<html>
<head>
<title>news feed</title>
<link rel="stylesheet" type="text/css" href="main/newsFeed/postCont/postCont.css">
</head>

<body>
	<?php 

		require "main/newsFeed/makePost.html";

				include_once 'includes/dbh.inc.php';
				$sql = "SELECT * FROM posts";
				$result = mysqli_query($conn, $sql);

				if (mysqli_num_rows($result) > 0) {
					while ($row = mysqli_fetch_assoc($result)) {
						$id = $row['puserid'];
						$userPost =  $row['pid'];
						
						$sqlimg = "SELECT * FROM profileimg WHERE userid = '$id'";
						$resultImg = mysqli_query($conn, $sqlimg);					
						while ($rowImg = mysqli_fetch_assoc($resultImg)) {


				echo"<div class='photoPostCont'>"; 
					echo"<div class='contMargin'>"; 
						echo"<div class='post'>"; 


							echo"<div id='pstcontent'>"; 
								echo"<div id='profile_pic'>"; 
									echo"<img class='post_img' src='main/newsFeed/post/img/".$userPost."'>";
							 echo"</div>";
							  echo"</div>";



							echo"<div id='pstInfoTop'>"; 



								echo"<div class='userPhoto'>"; 
									echo"<img class='post_prof_img' src='main/profile/uploads/profile".$id.".jpg?'>";
								echo"</div>";
								


									$sql_udata = "SELECT * FROM users WHERE user = '$id'";
								$result_udata = mysqli_query($conn, $sql_udata);		
							
								$row_udata = mysqli_fetch_assoc($result_udata);


							echo"<div class='userName'>"; echo $row_udata['username'];
								echo "<div class='UsrPstMeta'>";  echo '@_'; echo $row_udata['frstName']; echo' '; echo $row_udata['scndName'];echo "</div>";	

								
			        echo"<div class='skilltagcont'>";


									$select_column_name = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'skilltags' ORDER BY ORDINAL_POSITION
																";
									 		$resultTbleNme = mysqli_query($conn, $select_column_name);
									 		$datas = array();

											 if (mysqli_num_rows($resultTbleNme) > 0) {
									 			 while ($row1 = mysqli_fetch_assoc($resultTbleNme)) {
										 	 	$datas[] = $row1;
									 				 }
												 }

											 $arrayLength = count($datas);
											 $i = 0;
											 while ($i < $arrayLength) {

											foreach ($datas[$i] as $data) {
											$ADDUNION = " UNION ";
											$result1 = "SELECT '{$data}' AS column_name, {$data} AS column_value FROM skilltags WHERE uid = {$id} ";

											if ($i + 1 >=  $arrayLength) {
													$FINRESULT = $result1;
											}else{
												$FINRESULT = $result1." ".$ADDUNION;
											}

											$getresult = mysqli_query($conn,$result1);
											$row1 = mysqli_fetch_assoc($getresult);

											if ($row1['column_value'] >= 1) {
											echo "<div class='skilltag'>"; echo print_r($row1['column_name']); echo"</div>";

													}		
										 		$i++;
												}
											}	
					echo"</div>";
											echo "<div class='projectDescription'>"; 


											echo"</div>";






							echo"</div>";





echo"</div>";
				echo"</div>";
				    echo"</div>";
				        echo"</div>";

	

						}
					}
				}

	  ?>

	<div class="photoPostCont">

		<div class="contMargin">
				<div class="post">
			

			<div id="pstcontent"><div id="profile_pic"> <img class="post_img"  src="https://source.unsplash.com/random"></div></div>

			<div id="pstInfoTop">
					<div class="userPhoto">
						<div >
							<img class="post_img"  src="https://source.unsplash.com/random">
					</div>
				</div>


					<div class="userName">
						Tino Kingstone <div class="UsrPstMeta">@SonOfKings</div> 

						<div class="skilltagcont">
							<div class="skilltag">Music Producer</div>
							<div class="skilltag">3d Artist</div>
						</div>


						<div class="timePostes">. 12hr</div>
					</div>
				</div>
			

		</div>
		</div>
	</div>

<div class="btmBuffer" style="width: 100%; height:200px; display: inline-block; float: left; background-color: ;">
	
</div>

</body>

</html>




