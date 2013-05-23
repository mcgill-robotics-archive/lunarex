/* Auto-generated by genmsg_cpp for file /home/seb/McGill_LunarEx_2013/ROS_workspace/kinect_node/srv/kinectSafeDistance.srv */
#ifndef KINECT_NODE_SERVICE_KINECTSAFEDISTANCE_H
#define KINECT_NODE_SERVICE_KINECTSAFEDISTANCE_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "ros/service_traits.h"




namespace kinect_node
{
template <class ContainerAllocator>
struct kinectSafeDistanceRequest_ {
  typedef kinectSafeDistanceRequest_<ContainerAllocator> Type;

  kinectSafeDistanceRequest_()
  : request(0)
  {
  }

  kinectSafeDistanceRequest_(const ContainerAllocator& _alloc)
  : request(0)
  {
  }

  typedef int32_t _request_type;
  int32_t request;


  typedef boost::shared_ptr< ::kinect_node::kinectSafeDistanceRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::kinect_node::kinectSafeDistanceRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct kinectSafeDistanceRequest
typedef  ::kinect_node::kinectSafeDistanceRequest_<std::allocator<void> > kinectSafeDistanceRequest;

typedef boost::shared_ptr< ::kinect_node::kinectSafeDistanceRequest> kinectSafeDistanceRequestPtr;
typedef boost::shared_ptr< ::kinect_node::kinectSafeDistanceRequest const> kinectSafeDistanceRequestConstPtr;


template <class ContainerAllocator>
struct kinectSafeDistanceResponse_ {
  typedef kinectSafeDistanceResponse_<ContainerAllocator> Type;

  kinectSafeDistanceResponse_()
  : distance(0)
  {
  }

  kinectSafeDistanceResponse_(const ContainerAllocator& _alloc)
  : distance(0)
  {
  }

  typedef int32_t _distance_type;
  int32_t distance;


  typedef boost::shared_ptr< ::kinect_node::kinectSafeDistanceResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::kinect_node::kinectSafeDistanceResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct kinectSafeDistanceResponse
typedef  ::kinect_node::kinectSafeDistanceResponse_<std::allocator<void> > kinectSafeDistanceResponse;

typedef boost::shared_ptr< ::kinect_node::kinectSafeDistanceResponse> kinectSafeDistanceResponsePtr;
typedef boost::shared_ptr< ::kinect_node::kinectSafeDistanceResponse const> kinectSafeDistanceResponseConstPtr;

struct kinectSafeDistance
{

typedef kinectSafeDistanceRequest Request;
typedef kinectSafeDistanceResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct kinectSafeDistance
} // namespace kinect_node

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::kinect_node::kinectSafeDistanceRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::kinect_node::kinectSafeDistanceRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::kinect_node::kinectSafeDistanceRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "650f0ccd41c8f8d53ada80be6ddde434";
  }

  static const char* value(const  ::kinect_node::kinectSafeDistanceRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x650f0ccd41c8f8d5ULL;
  static const uint64_t static_value2 = 0x3ada80be6ddde434ULL;
};

template<class ContainerAllocator>
struct DataType< ::kinect_node::kinectSafeDistanceRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "kinect_node/kinectSafeDistanceRequest";
  }

  static const char* value(const  ::kinect_node::kinectSafeDistanceRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::kinect_node::kinectSafeDistanceRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "int32 request\n\
\n\
";
  }

  static const char* value(const  ::kinect_node::kinectSafeDistanceRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::kinect_node::kinectSafeDistanceRequest_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::kinect_node::kinectSafeDistanceResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::kinect_node::kinectSafeDistanceResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::kinect_node::kinectSafeDistanceResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "680f8923bb6b23ec7057fffc11ea7b34";
  }

  static const char* value(const  ::kinect_node::kinectSafeDistanceResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x680f8923bb6b23ecULL;
  static const uint64_t static_value2 = 0x7057fffc11ea7b34ULL;
};

template<class ContainerAllocator>
struct DataType< ::kinect_node::kinectSafeDistanceResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "kinect_node/kinectSafeDistanceResponse";
  }

  static const char* value(const  ::kinect_node::kinectSafeDistanceResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::kinect_node::kinectSafeDistanceResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "int32 distance\n\
\n\
\n\
";
  }

  static const char* value(const  ::kinect_node::kinectSafeDistanceResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::kinect_node::kinectSafeDistanceResponse_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::kinect_node::kinectSafeDistanceRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.request);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct kinectSafeDistanceRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::kinect_node::kinectSafeDistanceResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.distance);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct kinectSafeDistanceResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<kinect_node::kinectSafeDistance> {
  static const char* value() 
  {
    return "08ce175063802de56af0355992d6d2f3";
  }

  static const char* value(const kinect_node::kinectSafeDistance&) { return value(); } 
};

template<>
struct DataType<kinect_node::kinectSafeDistance> {
  static const char* value() 
  {
    return "kinect_node/kinectSafeDistance";
  }

  static const char* value(const kinect_node::kinectSafeDistance&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<kinect_node::kinectSafeDistanceRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "08ce175063802de56af0355992d6d2f3";
  }

  static const char* value(const kinect_node::kinectSafeDistanceRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<kinect_node::kinectSafeDistanceRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "kinect_node/kinectSafeDistance";
  }

  static const char* value(const kinect_node::kinectSafeDistanceRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<kinect_node::kinectSafeDistanceResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "08ce175063802de56af0355992d6d2f3";
  }

  static const char* value(const kinect_node::kinectSafeDistanceResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<kinect_node::kinectSafeDistanceResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "kinect_node/kinectSafeDistance";
  }

  static const char* value(const kinect_node::kinectSafeDistanceResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // KINECT_NODE_SERVICE_KINECTSAFEDISTANCE_H
