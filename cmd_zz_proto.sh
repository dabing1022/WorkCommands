source_path='/Users/ChildhoddAndy/Documents/ChildhoodAndy/zhuanzhuan/gitlab/Protobuf-Files'
des_path='/Users/ChildhoddAndy/ZZPods/ZZIM/ZZIM/Classes/PB'

protoc $source_path/zzbase.proto $source_path/zzuser.proto $source_path/zzmsg.proto --proto_path=$source_path/ --objc_out=$source_path/

cp $source_path/Zzbase.pbobjc.h $des_path/Zzbase.pbobjc.h
cp $source_path/Zzbase.pbobjc.m $des_path/Zzbase.pbobjc.m

cp $source_path/Zzuser.pbobjc.h $des_path/Zzuser.pbobjc.h
cp $source_path/Zzuser.pbobjc.m $des_path/Zzuser.pbobjc.m

cp $source_path/Zzmsg.pbobjc.h $des_path/Zzmsg.pbobjc.h
cp $source_path/Zzmsg.pbobjc.m $des_path/Zzmsg.pbobjc.m
